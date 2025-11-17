# CodeRoad LangGraph Workshop

Welcome to the LangGraph Workshop! This repository contains a series of hands-on Python scripts designed to teach you the fundamentals and advanced features of [LangGraph](https://langchain-ai.github.io/langgraph/), a library for building stateful, multi-actor applications with LLMs.

Each task in this workshop is a self-contained demonstration of a core LangGraph concept.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8+
- An active Google API Key with the Gemini API enabled.
- [uv] (https://docs.astral.sh/uv/getting-started/installation/) 

## ⚙️ Setup Instructions

Follow these steps to set up your local environment.

### 1. Clone the Repository

```bash
git clone https://github.com/rayner-villalba-coderoad-com/coderoad-langgraph-workshop.git
cd langgraph-workshop
```

### 2. Create a Virtual Environment (Option 1)

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```
### 2.1 Install Dependencies (Option 1)

Install all the required Python packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
``` 
### 3. Install Dependencies (Option 2)

Install all the required Python packages using the following uv command.

```bash
 uv add \          
  langgraph langchain langchain-core langchain-community \
  langchain-google-genai langgraph-checkpoint \
  ddgs beautifulsoup4 requests python-dotenv pydantic typing-extensions \
  streamlit
```

### 4. Set Environment Variables

This project requires a Google API key to interact with the Gemini models. Create a file named `.env` in the root of the project directory and add your key:

```.env
GOOGLE_API_KEY="your-google-api-key-here"
GOOGLE_MODEL="gemini-1.5-flash"
```

The scripts are configured to load these variables.

## 🚀 How to Execute the Commands

Each task is a runnable Python script located in its corresponding `task*/` directory. To run a specific task, navigate to the project's root directory and execute the script using Python.

For example, to run the demo for Task 2 (`stategraph_demo.py`):

```bash
uv run --env-file .env -- python task2/stategraph_demo.py
```

To run the final research assistant from Task 8:

```bash
uv run --env-file .env -- python task8/research_assistant.py
```

In case you are using pip install 
```bash
pip install python-dotenv
```
Load the .env file in your Python Script

```python
    import os
    from dotenv import load_dotenv

    # Load environment variables from .env file
    load_dotenv()

    # Access the environment variables
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
```

### Running the Streamlit Web App (Task 8)

Task 8 includes an interactive web application built with Streamlit. To run it, use the `streamlit run` command:

```bash
streamlit run task8/streamlit_app.py
```