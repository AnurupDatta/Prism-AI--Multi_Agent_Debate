import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from core.llm import MODEL_NAME

# Load environment variables from .env file
load_dotenv()

def get_judge_agent():
    """
    Initializes and returns the Final Judge Agent chain.

    This function sets up the agent by:
    1. Loading the system prompt for the judge from a file.
    2. Creating a chat prompt template that takes the original query,
       research output, critique, and bias analysis.
    3. Initializing the ChatGroq LLM.
    4. Combining them into a sequential chain.
    """
    # Get the absolute path to the prompt file
    prompt_path = os.path.join(os.path.dirname(__file__), '..', 'prompts', 'judge_prompt.txt')

    # Read the system prompt from the file
    with open(prompt_path, 'r') as f:
        system_prompt = f.read().strip()

    # Create a prompt template. It expects multiple inputs.
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", """
        Here is the information to synthesize:

        Original Query: {query}

        ---
        Initial Research Output:
        {research_output}

        ---
        Critique of the Research:
        {critique}

        ---
        Bias Analysis of the Research:
        {bias_report}
        
        ---
        Please provide your final, synthesized answer based on all the above information, followed by your confidence score.
        """)
    ])

    # Initialize the LLM
    llm = ChatGroq(
        temperature=0.2, # A bit of creativity for a well-rounded synthesis
        model_name=MODEL_NAME,
        api_key=os.getenv("GROQ_API_KEY")
    )

    # Create the chain
    chain = prompt | llm | StrOutputParser()

    return chain

if __name__ == '__main__':
    # This is a simple test to see if the agent works
    judge_agent = get_judge_agent()
    
    # Example inputs for testing
    sample_query = "Is nuclear energy a good solution for our future energy needs?"
    sample_research = "Nuclear energy is clean, efficient, and safe. It produces no emissions and is a reliable power source."
    sample_critique = "The research ignores the significant problems of nuclear waste disposal, high construction costs, and the risk of catastrophic accidents. It also fails to mention public opposition."
    sample_bias_report = "The initial research presents a one-sided, overly positive view, which can be considered a pro-nuclear bias. It omits key negative factors."

    response = judge_agent.invoke({
        "query": sample_query,
        "research_output": sample_research,
        "critique": sample_critique,
        "bias_report": sample_bias_report
    })
    print("--- Final Judge Agent Response ---")
    print(response)