# 🚀 Prism AI: A Multi-Agent Debate System

Prism AI is an advanced system that goes beyond traditional single-LLM responses. It simulates a debate between multiple specialized AI agents to produce a final answer that is comprehensive, critically evaluated, and checked for bias.

## ✨ Key Features

-   **Multi-Agent Architecture**: Utilizes a team of AI agents (Researcher, Critic, Bias Detector, and Judge) to analyze a query from multiple perspectives.
-   **Emergent Reasoning**: Through a structured debate loop, the system fosters a deeper level of reasoning than a single agent could achieve alone.
-   **Confidence Scoring**: The final answer includes a confidence score, providing insight into the strength of the consensus.
-   **Interactive UI**: A real-time Streamlit interface visualizes the "thinking process" of each agent.
-   **API Backend**: A robust FastAPI backend allows for easy integration with other services.

## 🏛️ High-Level Architecture

The system follows a clear, structured workflow:

`User Query` → `Research Agent` → (`Critic Agent` + `Bias Detector`) → `Final Judge` → `Final Answer + Confidence Score`

---

## 🖼️ Project Showcase

### 1. Interactive Streamlit UI

The primary interface for Prism AI. It shows the final verdict prominently, along with the confidence score.

![Final UI View](screenshots/ui_final_verdict.png)

Users can expand the cards to see the detailed output from each agent in the debate, providing full transparency into the reasoning process.

![Expanded UI View](screenshots/ui_expanded_view.png)

### 2. FastAPI Backend

The system is powered by a FastAPI server that exposes a `/debate` endpoint.

#### Interactive API Docs

The backend includes auto-generated documentation, making it easy to test and understand the API.

![FastAPI Docs](screenshots/backend_fastapi_docs.png)

#### API Client Usage

The endpoint can be easily called from any API client like Postman or integrated into other applications.

![API Client](screenshots/backend_api_client.png)

---

## 🛠️ Tech Stack

-   **Orchestration**: `LangGraph`
-   **LLM Integration**: `LangChain`
-   **LLM Provider**: `Groq` (for high-speed inference)
-   **Backend**: `FastAPI`
-   **Frontend**: `Streamlit`

---

## ⚙️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-folder>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API key:**
    -   Create a file named `.env` in the root of the project.
    -   Add your Groq API key to the file:
        ```
        GROQ_API_KEY=your_groq_api_key
        ```

---

## 🚀 How to Run

You can run either the interactive UI or the backend server.

### Running the Streamlit UI

This is the recommended way to interact with the project.

```bash
streamlit run ui.py
```

### Running the FastAPI Backend

If you want to interact with the API directly:

```bash
python app.py
```

You can then access the interactive documentation at `http://127.0.0.1:8000/docs`.
