import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from core.llm import MODEL_NAME

# Load environment variables from .env file
load_dotenv()

def get_critic_agent():
    """
    Initializes and returns the Critic Agent chain.

    This function sets up the agent by:
    1. Loading the system prompt for the critic from a file.
    2. Creating a chat prompt template that takes the research output.
    3. Initializing the ChatGroq LLM.
    4. Combining them into a sequential chain.
    """
    # Get the absolute path to the prompt file
    prompt_path = os.path.join(os.path.dirname(__file__), '..', 'prompts', 'critic_prompt.txt')

    # Read the system prompt from the file
    with open(prompt_path, 'r') as f:
        system_prompt = f.read().strip()

    # Create a prompt template. It expects the research output as input.
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "Here is the research output to critique:\n\n{research_output}")
    ])

    # Initialize the LLM
    llm = ChatGroq(
        temperature=0.1, # A little more creative to find flaws
        model_name=MODEL_NAME,
        api_key=os.getenv("GROQ_API_KEY")
    )

    # Create the chain
    chain = prompt | llm | StrOutputParser()

    return chain

if __name__ == '__main__':
    # This is a simple test to see if the agent works
    critic_agent = get_critic_agent()
    
    # Example research output for testing
    sample_research_output = """
    Nuclear energy is a powerful and efficient source of electricity. 
    It produces no greenhouse gas emissions during operation, making it a key tool in fighting climate change. 
    The fuel, uranium, is abundant, and modern plants are extremely safe.
    """
    
    response = critic_agent.invoke({"research_output": sample_research_output})
    print("--- Critic Agent Response ---")
    print(response)