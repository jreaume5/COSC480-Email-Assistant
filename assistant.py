import base64
import os
from email.message import EmailMessage
from googleapiclient.discovery import build
from ollama import Client


client = Client(host='http://localhost:11434')

def create_draft(service, user_id, sender, subject, body):
    message = EmailMessage()
    message.set_content(body)
    message['To'] = sender
    message['From'] = 'me'
    message['Subject'] = f"Re: {subject}"

    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    create_message = {'message': {'raw': encoded_message}}
    draft = service.users().drafts().create(userId=user_id, body=create_message).execute()
    print(f'Draft id: {draft["id"]} created.')
    return draft

while True:
    prompt = input(">>> ")
    if prompt.lower() in ['exit', 'quit']:
        break

    # Get the full response from Gemma
    response = client.chat(
        model='gemma3:1b',
        messages=[
            {'role': 'system', 'content': 'You are a professional email assistant. Always start with "Subject:" followed by "Body:".'},
            {'role': 'user', 'content': prompt}
        ]
    )
    
    full_text = response['message']['content']
    print(f"\nAI Generated:\n{full_text}\n")

    # Basic parsing logic
    if "Subject:" in full_text and "Body:" in full_text:
        try:
            subject = full_text.split("Subject:")[1].split("Body:")[0].strip()
            body = full_text.split("Body:")[1].strip()
            
            confirm = input("Create Gmail draft? (y/n): ")
            if confirm.lower() == 'y':
                # 'service' must be initialized earlier in your script
                create_draft(service, 'me', 'recipient@example.com', subject, body)
        except Exception as e:
            print(f"Error parsing email structure: {e}")
    else:
        print("AI did not follow the Subject/Body format. Try again.")
