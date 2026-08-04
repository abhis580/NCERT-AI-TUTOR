import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

def load_llm():

    load_dotenv()

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        google_api_key=GOOGLE_API_KEY
    )

    return llm