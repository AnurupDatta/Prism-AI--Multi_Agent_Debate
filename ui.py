# ui.py
import streamlit as st
import re # Import the regular expression module
from graph.workflow import build_graph

# --- Page Configuration ---
st.set_page_config(
    page_title="Prism AI : Multi-Agent Debate System",
    page_icon="🚀",
    layout="wide"
)

# --- Header ---
st.title("🚀 Prism AI : Multi-Agent Debate System")
st.markdown("""
Welcome! Enter a query and see how AI agents debate to find the best answer. 
The initial research, critique, and bias report will appear below as collapsed cards. Click to expand them. The final verdict will be displayed at the bottom.
""")

# --- Main Application ---

@st.cache_resource
def get_debate_graph():
    return build_graph()

debate_graph = get_debate_graph()

query = st.text_input(
    "Enter your query:",
    placeholder="e.g., What are the pros and cons of remote work?",
    value="Should social media platforms be regulated by the government?"
)

if st.button("Start Debate"):
    if not query:
        st.warning("Please enter a query to start the debate.")
    else:
        st.info("The debate has started... The agent responses will appear below.")

        initial_state = {"query": query}
        
        col1, col2, col3 = st.columns(3)
        with col1:
            researcher_placeholder = st.empty()
        with col2:
            critic_placeholder = st.empty()
        with col3:
            bias_placeholder = st.empty()
        
        judge_placeholder = st.empty()

        for step in debate_graph.stream(initial_state):
            node_name = list(step.keys())[0]
            node_output = step[node_name]

            if node_name == "researcher":
                with researcher_placeholder.container():
                    with st.expander("🔍 Research Agent's Findings", expanded=False):
                        st.markdown(node_output['research_output'])
            
            elif node_name == "critic":
                with critic_placeholder.container():
                    with st.expander("🧨 Critic Agent's Analysis", expanded=False):
                        st.markdown(node_output['critique'])

            elif node_name == "bias_detector":
                with bias_placeholder.container():
                    with st.expander("⚖️ Bias Detector's Report", expanded=False):
                        st.markdown(node_output['bias_report'])

            elif node_name == "judge":
                with judge_placeholder.container():
                    st.success("🏆 The Final Verdict")
                    
                    # --- NEW: Extract and Display the Score ---
                    final_text = node_output['final_answer']
                    score = 0 # Default score
                    
                    # Use a regular expression to find a number after "Confidence Score"
                    # This looks for "Confidence Score", optional colon/space, and then captures the number
                    match = re.search(r"Confidence Score:?\s*(\d+)", final_text, re.IGNORECASE)
                    
                    if match:
                        # If a score is found, convert it to an integer
                        score = int(match.group(1))
                        # Optionally, remove the score line from the final text to avoid showing it twice
                        final_text = re.sub(r"Confidence Score:?\s*\d+%", "", final_text, flags=re.IGNORECASE).strip()

                    # Display the score using the attractive st.metric component
                    st.metric(label="Confidence Score", value=f"{score}%")
                    
                    # Display the final answer text
                    st.markdown(final_text)

# --- Footer ---
st.markdown("---")
st.markdown("Built with LangGraph, Streamlit, and Groq.")