from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="D:\\self\\NLP\\Projects\\Log classification\\.env")
print("os.environ.get:", os.environ.get("GROQ_API_KEY"))
print("os.getenv:", os.getenv("GROQ_API_KEY"))