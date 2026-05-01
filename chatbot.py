from ollama import Client


client = Client(host='http://localhost:11434')

while(True):
    prompt = input(">>> ")


    if prompt.lower() in ['exit', 'quit']:
        break

    # Get the full response from Google Gemma 3 1b
    response = client.chat(
        model='gemma3:1b',
        messages=[
            {'role': 'system', 'content': 'You are a friendly chatbot designed to make others happy. Make sure your responses are also less than 250 characters.'},
            {'role': 'user', 'content': prompt}
        ]
    )
    
    full_text = response['message']['content']
    print(f"\n{full_text}\n")
