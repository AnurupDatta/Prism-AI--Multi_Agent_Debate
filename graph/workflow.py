from typing import TypedDict
from langgraph.graph import StateGraph, END
from agents.llama_agent import create_llama_chain
from agents.qwen_agent import create_qwen_chain
from agents.gemini_agent import create_gemini_chain
from agents.judge_agents import create_judge_chain

# --- Graph State ---
class DebateState(TypedDict):
    query: str
    llama_answer: str
    qwen_answer: str
    gemini_answer: str
    final_answer: str

# --- Node Functions ---

def llama_node(state: DebateState):
    """Invokes the Llama 3 debater agent."""
    query = state["query"]
    chain = create_llama_chain()
    response = chain.invoke({"query": query})
    return {"llama_answer": response}

def qwen_node(state: DebateState):
    """Invokes the Qwen debater agent."""
    query = state["query"]
    chain = create_qwen_chain()
    response = chain.invoke({"query": query})
    return {"qwen_answer": response}

def gemini_node(state: DebateState):
    """Invokes the Gemini debater agent."""
    query = state["query"]
    chain = create_gemini_chain()
    response = chain.invoke({"query": query})
    return {"gemini_answer": response}

def judge_node(state: DebateState):
    """Invokes the Judge agent to synthesize the final answer."""
    chain = create_judge_chain()
    # Note: The judge prompt uses a generic key `claude_answer` but we pass qwen's output to it.
    # This is fine as long as we are consistent.
    response = chain.invoke({
        "query": state["query"],
        "llama_answer": state["llama_answer"],
        "qwen_answer": state["qwen_answer"],
        "gemini_answer": state["gemini_answer"],
    })
    return {"final_answer": response}

# --- Graph Builder ---

def build_graph():
    """Builds the multi-agent debate graph."""
    workflow = StateGraph(DebateState)

    workflow.add_node("llama_debater", llama_node)
    workflow.add_node("qwen_debater", qwen_node)
    workflow.add_node("gemini_debater", gemini_node)
    workflow.add_node("judge", judge_node)

    workflow.set_entry_point("llama_debater")
    workflow.set_entry_point("qwen_debater")
    workflow.set_entry_point("gemini_debater")

    workflow.add_edge("llama_debater", "judge")
    workflow.add_edge("qwen_debater", "judge")
    workflow.add_edge("gemini_debater", "judge")

    workflow.add_edge("judge", END)

    debate_graph = workflow.compile()
    return debate_graph