from typing import TypedDict, List
from langgraph.graph import StateGraph, END

# Import the agent functions we created
from agents.research_agents import get_research_agent
from agents.critic_agents import get_critic_agent
from agents.bias_agents import get_bias_agent
from agents.judge_agents import get_judge_agent

# 1. Define the State
class DebateState(TypedDict):
    """
    Represents the state of our debate.
    It holds all the data that flows through the graph.
    """
    query: str
    research_output: str
    critique: str
    bias_report: str
    final_answer: str

# 2. Define the Nodes
def run_researcher(state: DebateState):
    """
    Runs the research agent and updates the state.
    """
    print("---NODE: Running Researcher---")
    query = state['query']
    research_agent = get_research_agent()
    research_output = research_agent.invoke({"query": query})
    return {"research_output": research_output}

def run_critic(state: DebateState):
    """
    Runs the critic agent and updates the state.
    """
    print("---NODE: Running Critic---")
    research_output = state['research_output']
    critic_agent = get_critic_agent()
    critique = critic_agent.invoke({"research_output": research_output})
    return {"critique": critique}

def run_bias_detector(state: DebateState):
    """
    Runs the bias detector agent and updates the state.
    """
    print("---NODE: Running Bias Detector---")
    research_output = state['research_output']
    bias_agent = get_bias_agent()
    bias_report = bias_agent.invoke({"research_output": research_output})
    return {"bias_report": bias_report}

def run_judge(state: DebateState):
    """
    Runs the final judge agent and updates the state with the final answer.
    """
    print("---NODE: Running Final Judge---")
    judge_agent = get_judge_agent()
    final_answer = judge_agent.invoke({
        "query": state['query'],
        "research_output": state['research_output'],
        "critique": state['critique'],
        "bias_report": state['bias_report']
    })
    return {"final_answer": final_answer}

# 3. Build the Graph
def build_graph():
    """
    Builds the LangGraph workflow.
    """
    # Initialize the graph with our state definition
    builder = StateGraph(DebateState)

    # Add the nodes
    builder.add_node("researcher", run_researcher)
    builder.add_node("critic", run_critic)
    builder.add_node("bias_detector", run_bias_detector)
    builder.add_node("judge", run_judge)

    # Add the edges to define the flow
    builder.set_entry_point("researcher")
    builder.add_edge("researcher", "critic")
    builder.add_edge("researcher", "bias_detector")
    
    # The critic and bias detector both lead to the judge
    builder.add_edge("critic", "judge")
    builder.add_edge("bias_detector", "judge")

    builder.add_edge("judge", END)

    # Compile the graph
    graph = builder.compile()
    return graph

if __name__ == '__main__':
    # This is a test to run the entire workflow
    graph = build_graph()
    
    # The input to the graph is the initial state
    initial_state = {"query": "Should social media platforms be regulated by the government?"}
    
    # Invoke the graph and stream the results
    for step in graph.stream(initial_state):
        # The step is a dictionary with the node name as the key
        node_name = list(step.keys())[0]
        print(f"--- Output of: {node_name} ---")
        print(step[node_name])
        print("\n")
