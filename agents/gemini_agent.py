from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from core.llm import gemini_llm

# Load the debater prompt from the file
with open("prompts/debater_prompt.txt", "r") as f:
    debater_prompt_template = f.read()

def create_gemini_chain():
    """
    Creates a LangChain chain for the Gemini debater agent.
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", debater_prompt_template),
        ("human", "{query}")
    ])
    
    chain = prompt | gemini_llm | StrOutputParser()
    return chain