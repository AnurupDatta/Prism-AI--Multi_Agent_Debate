from fastapi import FastAPI
from pydantic import BaseModel
from graph.workflow import build_graph
import uvicorn

# Initialize the FastAPI app
app = FastAPI(
    title="Multi-Agent Debate System API",
    description="An API for running a multi-agent debate to answer user queries.",
    version="1.0.0"
)

# Build the graph once when the application starts up
debate_graph = build_graph()

# Define the request body model
class DebateRequest(BaseModel):
    query: str

# --- NEW: Updated Response Model ---
# This model now includes fields for every agent's output.
class DebateResponse(BaseModel):
    research_output: str
    critique: str
    bias_report: str
    final_answer: str

# Define the main API endpoint
# The response_model now points to our new, more detailed DebateResponse
@app.post("/debate", response_model=DebateResponse)
async def run_debate_endpoint(request: DebateRequest):
    """
    Accepts a user query, runs it through the multi-agent debate graph,
    and returns the final, synthesized answer along with all intermediate steps.
    """
    # Prepare the initial state for the graph
    initial_state = {"query": request.query}
    
    # Invoke the graph. The final_state will contain all the outputs.
    final_state = debate_graph.invoke(initial_state)

    return final_state

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)