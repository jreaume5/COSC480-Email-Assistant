from ollama import Client

client = Client(host='http://localhost:11434')

while True:
    prompt = input(">>> ")
    for chunk in client.chat(
        model='gemma3:1b',
        messages=[{'role': 'system', 'content': 'Keep responses as brief as possible.'}, {'role': 'user', 'content': prompt}],
        stream=True
    ):
        print(chunk['message']['content'], end='', flush=True)
    print()  # newline at end
