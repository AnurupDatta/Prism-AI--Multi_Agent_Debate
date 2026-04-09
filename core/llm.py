import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

# 1. Llama 3 model via Groq for the first debater
llama_llm = ChatGroq(
    api_key=os.environ.get("GROQ_API_KEY"),
    model="llama-3.1-8b-instant",
    temperature=0.7,
)

# 2. Claude 3 Haiku model via Anthropic for the second debater
qwen_llm = ChatGroq(
    api_key=os.environ.get("GROQ_API_KEY"),
    model="qwen/qwen3-32b",
    temperature=0.7,
)

# 3. Gemini Pro model via Google for the third debater
gemini_llm = ChatGoogleGenerativeAI(
    google_api_key=os.environ.get("GOOGLE_API_KEY"),
    model="gemini-2.5-flash-lite",
    temperature=0.7,
)


judge_llm = ChatGroq(
    api_key=os.environ.get("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
    temperature=0.4, # Lower temperature for more deterministic judging
)