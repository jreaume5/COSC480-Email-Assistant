from ollama import Client

client = Client(host='http://localhost:11434')

for chunk in client.chat(
    model='gemma3:1b',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True
):
    print(chunk['message']['content'], end='', flush=True)
print()  # newline at end
