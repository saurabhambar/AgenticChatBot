# End to End Project – Agentic AI Chatbot

## Project Overview

This project is part of an end-to-end implementation where we start by building a **basic chatbot** using modular coding practices.

As we progress, the complexity of the applications will increase:

- Basic Chatbot  
- Chatbot with Tools  
- Fetching Recent AI News  
- More complex projects using FastAPI  
- Deployment using CI/CD pipeline  

Initially, we begin with building a **basic chatbot**.

---

# Setup Environment

## 1. Create Project Workspace

First, create a dedicated project folder in your local system.

Example:

AgenticChatBot

Open Command Prompt in this folder and launch VS Code from there.

You can choose any location in your local system. All coding for this project will be done inside this project folder.

---

## 2. Create Virtual Environment

It is mandatory to create a separate environment for every project.

### Using Conda

```bash
conda create -p venv python==3.13
```

This creates a virtual environment named venv using Python 3.13.

When prompted to confirm package installation, type:

`y`

### Activate the environment:

`conda activate venv`

- Activation is case-sensitive on some systems; use the exact name you created (venv or Venv) depending on your command.

### Create requirements.txt

`requirements.txt`

### Add the libraries that will be used for this project. (List taken from the transcript; include these lines in requirements.txt.)

```bash
langchain
langgraph
langchain-community
langchain-core
langchain-groq
langchain-openai
faiss-cpu
streamlit
python-tavily
```

- Notes from transcript:

    - langchain-groq was preferred because it is open source.

    - langchain-openai is optional.

    - tavily / Tavileh is used for internet search.

### 4. Install Dependencies

- With the virtual environment activated, run:    

```pip install -r requirements.txt```

- Wait for the installation to complete — this will install all libraries listed in requirements.txt into your virtual environment.

### GitHub Preparation

- Before committing code to GitHub, add these files to your project.

### Create .gitignore

- Create a file named:

`.gitignore`

### Create README.md

- Create the project README file:

`README.md`

- Add an initial title/description (this file will be updated with project documentation).

- Example content:

`End to End Project – Agentic AI Chatbot`


### Alternative: UV (optional)

- If you prefer the UV workflow (used later in other demos), you can initialize a workspace with:

`pip3 install uv`
`uv init <folder_name>`
`uv add langgraph langchain_community langchain_core langchain_groq langchain_openai faiss_cpu streamlit tavily-python`
 


