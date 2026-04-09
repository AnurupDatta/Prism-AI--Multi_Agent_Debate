from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from core.llm import judge_llm

# Load the judge prompt from the file
with open("prompts/judge_prompt.txt", "r") as f:
    judge_prompt_template = f.read()

def create_judge_chain():
    """
    Creates a LangChain chain for the Judge agent.
    """
    prompt = ChatPromptTemplate.from_template(judge_prompt_template)
    
    chain = prompt | judge_llm | StrOutputParser()
    return chain