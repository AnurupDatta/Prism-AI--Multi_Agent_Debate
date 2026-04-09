import streamlit as st
import re
from graph.workflow import build_graph

# --- Page Configuration ---
st.set_page_config(
    page_title="Prism AI: Multi-Model Debate",
    page_icon="🚀",
    layout="wide"
)

# --- Header ---
st.title("🚀 Prism AI: Multi-Model Debate")
st.markdown("""
Welcome! Enter a query to start the debate. The final verdict will appear at the bottom. 
You can click on each debater's card to expand it and see their individual answer.
""")

# --- Main Application ---

@st.cache_resource
def get_debate_graph():
    """Caches the compiled LangGraph object."""
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
        
        # Placeholders for the debater and judge outputs
        col1, col2, col3 = st.columns(3)
        with col1:
            llama_placeholder = st.empty()
        with col2:
            qwen_placeholder = st.empty()
        with col3:
            gemini_placeholder = st.empty()
        
        judge_placeholder = st.empty()

        # Use expanders for agent responses
        with llama_placeholder:
            llama_expander = st.expander("🤖 Llama 3's Answer", expanded=False)
        with qwen_placeholder:
            qwen_expander = st.expander("🐉 Qwen 2's Answer", expanded=False)
        with gemini_placeholder:
            gemini_expander = st.expander("✨ Gemini's Answer", expanded=False)

        # Stream the graph execution
        for step in debate_graph.stream(initial_state):
            node_name = list(step.keys())[0]
            node_output = step[node_name]

            if node_name == "llama_debater":
                llama_expander.markdown(node_output['llama_answer'])
            
            elif node_name == "qwen_debater":
                qwen_expander.markdown(node_output['qwen_answer'])

            elif node_name == "gemini_debater":
                gemini_expander.markdown(node_output['gemini_answer'])

            elif node_name == "judge":
                with judge_placeholder.container():
                    st.success("🏆 The Final Verdict")
                    
                    final_text = node_output['final_answer']
                    score = 0 # Default score
                    
                    # Use regex to find the confidence score
                    match = re.search(r"Confidence Score:?\s*(\d+)", final_text, re.IGNORECASE)
                    
                    if match:
                        score = int(match.group(1))
                        # Remove the score line from the final text
                        final_text = re.sub(r"Confidence Score:?\s*\d+%", "", final_text, flags=re.IGNORECASE).strip()

                    st.metric(label="Confidence Score", value=f"{score}%")
                    
                    # --- NEW: Display the final answer in bold ---
                    st.markdown(f"**{final_text.strip()}**")

# --- Footer ---
st.markdown("---")
st.markdown("Built by Anurup Datta.")