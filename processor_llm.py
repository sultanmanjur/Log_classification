from dotenv import load_dotenv
from groq import Groq
import os

# Load environment variables from .env file
load_dotenv(dotenv_path=".env")

# Debug print to confirm API key is loaded
print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))

# Initialize Groq client with API key
groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

prompt = 'What is the difference between Ai and Machine Learning?'

def classify_with_llm(log_message):
    prompt = f"""
    Classify the following log message into one of these categories:
    (1)Workflow Error, (2) Deprecation Warning. 
    If you cannot figure out a category, return "Unclassified".
    Only return the category name. No preamble, no postamble.
    Log message: {log_message}
    """
    chat_completion = groq.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    print(classify_with_llm("Lead conversion failed for prospect ID 7842 due to missing contact information."))
    print(classify_with_llm("The 'ExportToCSV' feature is outdated. Please migrate to 'ExportToXLSX' by the end of Q3"))
    print(classify_with_llm("System reboot initiated by user AdminUser."))