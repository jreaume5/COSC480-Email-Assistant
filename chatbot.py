import base64
import os
from email.message import EmailMessage
from googleapiclient.discovery import build
from ollama import Client


client = Client(host='http://localhost:11434')

    if prompt.lower() in ['exit', 'quit']:
        break

    # Get the full response from Google Gemma 3 1b
    response = client.chat(
        model='gemma3:1b',
        messages=[
            {'role': 'system', 'content': 'You are a friendly chatbot designed to make others happy.'},
            {'role': 'user', 'content': prompt}
        ]
    )
    
    full_text = response['message']['content']
    print(f"\n{full_text}\n")
