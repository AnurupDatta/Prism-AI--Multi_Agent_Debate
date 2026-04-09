from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from core.llm import qwen_llm

# Load the debater prompt from the file
with open("prompts/debater_prompt.txt", "r") as f:
    debater_prompt_template = f.read()

def create_qwen_chain():
    """
    Creates a LangChain chain for the Qwen debater agent.
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", debater_prompt_template),
        ("human", "{query}")
    ])
    
    chain = prompt | qwen_llm | StrOutputParser()
    return chain