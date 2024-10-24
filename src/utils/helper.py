from dotenv import load_dotenv, find_dotenv

def load_env():
    dotenv_path = find_dotenv()
    print(f"Found .env file at: {dotenv_path}")

    if dotenv_path:
        result = load_dotenv(dotenv_path)
        print(f"load_dotenv() result: {result}")
    else:
        print("No .env file found")
