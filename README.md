### 1. Setup Device:
    - Make sure the Raspberry Pi is plugged in and on.
    - Remote into the Raspberry Pi (we recommended to use Raspberry Pi Connect).

### 2. Setup Virtual Environment:
    - python3 -m venv .venv
    - source .venv/bin/activate

### 3. Install Dependencies 
    - git clone https://github.com/jreaume5/COSC480-Chatbot.git
    - pip install -r requirements.txt
    - ollama pull gemma3:1b
    
### 4. Run Program
    - ollama serve
    - python3 chatbot.py
