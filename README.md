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

<img width="2876" height="1463" alt="Screenshot 2026-04-05 141056" src="https://github.com/user-attachments/assets/b080a85e-c481-4448-8117-99b90024300b" />

Users can expand the cards to see the detailed output from each agent in the debate, providing full transparency into the reasoning process.

<img width="2872" height="1422" alt="Screenshot 2026-04-05 141116" src="https://github.com/user-attachments/assets/df2290c4-8660-4c11-840b-30988a3f1574" />

### 2. FastAPI Backend

The system is powered by a FastAPI server that exposes a `/debate` endpoint.

#### Interactive API Docs

The backend includes auto-generated documentation, making it easy to test and understand the API.

<img width="2878" height="1421" alt="Screenshot 2026-04-05 141747" src="https://github.com/user-attachments/assets/28236821-8203-453f-ae77-f3adfe6f9a25" />

#### API Client Usage

The endpoint can be easily called from any API client like Postman or integrated into other applications.

<img width="2112" height="1525" alt="Screenshot 2026-04-05 141901" src="https://github.com/user-attachments/assets/ca8c7cd4-3c65-48d3-8751-e3075b55a8c3" />

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
