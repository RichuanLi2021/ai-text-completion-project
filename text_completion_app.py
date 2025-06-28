"""
AI_TEXT_COMPLETION

What is it?
it is a simple REPL that sends user prompts to GPT-3.5-turbo and prints the reply.
"""
from dotenv import load_dotenv
# load env file
env = load_dotenv() 

import os, sys, json, argparse
from openai import OpenAI, OpenAIError
from pathlib import Path 

# config
def get_api_key():
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        sys.exit("❌  OPENAI_API_KEY not set. export it first.")
    return key

MODEL = "gpt-3.5-turbo"

# initialize the new 1.x client (auto‑loads OPENAI_API_KEY from env)
client = OpenAI(api_key=get_api_key())

# helper
def complete(prompt: str, temperature: float, max_tokens: int) -> str:
    """
    Call OpenAI chat completion endpoint.
    Replace with HF/Cohere equivalent if needed.
    """
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content.strip()

# main REPL
def main():
    parser = argparse.ArgumentParser(
        description="Interactive GPT-3.5 prompt-completion app."
    )
    parser.add_argument(
        "-t", "--temperature", type=float, default=0.7,
        help="Creativity (0–2). 0 = deterministic."
    )
    parser.add_argument(
        "-m", "--max-tokens", type=int, default=150,
        help="Maximum tokens in the completion."
    )
    args = parser.parse_args()

    print("✨  Enter your prompt (empty line to quit).")

    
    while True:
        try:
            prompt = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋  Bye!")
            break

        if not prompt:
            print("👋  Bye!")
            break
        try:
            reply = complete(prompt, args.temperature, args.max_tokens)
            print(f"\n🧠 {reply}")
        except Exception as e:
            print(f"⚠️  Error: {e}")

if __name__ == "__main__":
    main()