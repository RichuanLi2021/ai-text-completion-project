## Setup
```bash
1. git clone to pull this project
git clone /url

2. create and activate venv
python3 -m venv .venv
source .venv/bin/activate
```

## Usage
This is a CLI REPL that takes in your prompts to a CHATGPT 3.5 from OPENAI and prints the response.  

You need to have your own OPEN API KEY to be in .env file to be used.

## Dependencies
- Install Dependencies
```bash
pip install -r requirements.txt   # or:
pip install openai python-dotenv tiktoken vllm
```