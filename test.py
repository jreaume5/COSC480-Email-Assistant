import requests
r = requests.get('http://localhost:11434/api/tags')
print(r.json())
