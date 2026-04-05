import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from core.llm import MODEL_NAME

# Load environment variables from .env file
load_dotenv()

def get_bias_agent():
    """
    Initializes and returns the Bias Detector Agent chain.

    This function sets up the agent by:
    1. Loading the system prompt for the bias detector from a file.
    2. Creating a chat prompt template that takes the research output.
    3. Initializing the ChatGroq LLM.
    4. Combining them into a sequential chain.
    """
    # Get the absolute path to the prompt file
    prompt_path = os.path.join(os.path.dirname(__file__), '..', 'prompts', 'bias_prompt.txt')

    # Read the system prompt from the file
    with open(prompt_path, 'r') as f:
        system_prompt = f.read().strip()

    # Create a prompt template. It expects the research output as input.
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "Here is the text to analyze for bias:\n\n{research_output}")
    ])

    # Initialize the LLM
    llm = ChatGroq(
        temperature=0, # We want a deterministic analysis of bias
        model_name=MODEL_NAME,
        api_key=os.getenv("GROQ_API_KEY")
    )

    # Create the chain
    chain = prompt | llm | StrOutputParser()

    return chain

if __name__ == '__main__':
    # This is a simple test to see if the agent works
    bias_agent = get_bias_agent()
    
    # Example research output with potential bias for testing
    sample_research_output = """
    Nuclear energy is the only sensible solution for the future. 
    Anyone who opposes it is simply ignoring science and holding back progress. 
    Countries that embrace it will become economic leaders, while others will fall behind.
    """
    
    response = bias_agent.invoke({"research_output": sample_research_output})
    print("--- Bias Detector Agent Response ---")
    print(response)