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
        
    for chunk in client.chat(
        model='gemma:2b', # Make sure this matches your downloaded model
        messages=[{'role': 'system', 'content': 'Keep responses as brief as possible.'}, 
                  {'role': 'user', 'content': prompt}],
        stream=True
    ):
        print(chunk['message']['content'], end='', flush=True)
    print() # newline at end
