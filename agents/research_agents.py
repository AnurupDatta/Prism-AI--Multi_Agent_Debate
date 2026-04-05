import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from core.llm import MODEL_NAME

# Load environment variables from .env file
load_dotenv()

def get_research_agent():
    """
    Initializes and returns the Research Agent chain.

    This function sets up the agent by:
    1. Loading the system prompt from a file.
    2. Creating a chat prompt template.
    3. Initializing the ChatGroq LLM.
    4. Combining them into a sequential chain.
    """
    # Get the absolute path to the prompt file
    prompt_path = os.path.join(os.path.dirname(__file__), '..', 'prompts', 'research_prompt.txt')

    # Read the system prompt from the file
    with open(prompt_path, 'r') as f:
        system_prompt = f.read().strip()

    # Create a prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{query}")
    ])

    # Initialize the LLM
    llm = ChatGroq(
        temperature=0,
        model_name=MODEL_NAME,
        api_key=os.getenv("GROQ_API_KEY")
    )

    # Create the chain
    chain = prompt | llm | StrOutputParser()

    return chain

if __name__ == '__main__':
    # This is a simple test to see if the agent works
    research_agent = get_research_agent()
    query = "What are the pros and cons of using nuclear energy?"
    response = research_agent.invoke({"query": query})
    print("--- Research Agent Response ---")
    print(response)
