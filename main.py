from dotenv import load_dotenv
from groq import Client
import os

load_dotenv()

def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmetic calculations with numbers"""
    print("Tool has been called.")
    return f"The sum of {a} and {b} is {a + b}"
    
def say_hello(name: str) -> str:
    """Useful for greeting a user"""
    print("Tool has been called.")
    return f"Hello {name}, I hope you are well today"

def main():
    client = Client(api_key=os.getenv("GROQ_API_KEY"))

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input == "quit":
            break

        # Call tools if input matches (very simple demo)
        if user_input.lower().startswith("calculate"):
            # Expect input like: calculate 3 4
            try:
                parts = user_input.split()
                a = float(parts[1])
                b = float(parts[2])
                print(calculator(a, b))
                continue
            except Exception:
                print("Please provide two numbers like: calculate 3 4")
                continue
        elif user_input.lower().startswith("hello"):
            # Expect input like: hello Alice
            try:
                name = user_input.split(maxsplit=1)[1]
                print(say_hello(name))
                continue
            except Exception:
                print("Please provide a name like: hello Alice")
                continue

        # Otherwise, send to Groq chat model
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": user_input}]
        )
        print("Assistant:", response.choices[0].message.content)

if __name__ == "__main__":
    main()
