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

### Add the libraries that will be used for this project.

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

- Notes:

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

```bash
pip3 install uv
uv init <folder_name>
uv add langgraph langchain_community langchain_core langchain_groq langchain_openai faiss_cpu streamlit tavily-python
```

# Architecture Flow Diagram

The project follows a **pipeline-based modular architecture** built around a complex workflow using LangGraph.

![alt text](project-structure.png)

The architecture consists of:

1. Frontend (Streamlit)
2. Workflow (Graph)
3. Independent Components
4. State Management
5. LLM Integration

---

## High-Level Flow

Frontend (Streamlit)  
        ↓  
State Initialization  
        ↓  
Graph Execution (Complex Workflow)  
        ↓  
Nodes (Independent Functional Components)  
        ↓  
LLMs + Function Execution  
        ↓  
Response Returned to UI  

---

## Component Explanation Based on Flow Diagram

### 1️⃣ UI (Frontend)

- Built using **Streamlit**
- Allows users to:
  - Select LLM
  - Select model
  - Provide API keys
  - Select use case
  - Enter chat message
- Triggers workflow execution
- Displays final response

The UI acts as the **entry point of execution**.

---

### 2️⃣ State

- Maintains shared information across nodes
- Stores conversation context
- Accessible throughout the workflow
- Ensures consistent data flow across the graph

State acts as the **central memory layer**.

---

### 3️⃣ Graph (Complex Workflow)

- Represents the full chatbot workflow
- Built using LangGraph
- Contains:
  - Start node
  - Functional nodes
  - Conditional edges
  - End node

The graph defines:
- How nodes are connected
- Execution order
- Conditional routing logic

Complex Workflow → Graph Representation

---

### 4️⃣ Nodes

Nodes are independent functional components.

Each node:
- Contains specific logic
- Executes a defined function
- May call an LLM
- Can connect to other nodes via edges

In the diagram:
- Node → Function 1 + LLM
- Node → Function 2 + LLM
- Node → Function 3 + LLM

Each node is implemented as a separate module for modularity.

---

### 5️⃣ LLMs

- Integrated within nodes
- Can support multiple models
- Selected dynamically from UI
- Used for response generation

LLMs are not tightly coupled to the UI — they are invoked through nodes.

---

## Execution Pipeline Concept

This project does NOT execute like a Jupyter Notebook.

Instead, it runs as a structured pipeline:

1. User input from UI
2. Workflow starts at Graph Start Node
3. Execution moves across nodes via edges
4. Conditional logic determines next step
5. Functions + LLMs execute
6. End node returns final output
7. Response displayed in UI

---

## Independent Modular Components

The architecture is built using independent modules:

- Nodes
- Graph
- LLMs
- State
- Tools
- UI

Each component is isolated in its own folder and treated as a package.

This ensures:

- Clean architecture
- Reusability
- Scalability
- Maintainability
- Deployment readiness

---

## Architectural Summary

The system follows this structure:

UI (Streamlit)  
        ↓  
State  
        ↓  
Graph (Workflow Engine)  
        ↓  
Nodes (Functions + LLMs)  
        ↓  
End Node  
        ↓  
UI Response  

This design enables:

- Modular development
- Complex workflow orchestration
- LLM abstraction
- Tool integration
- Clean CI/CD deployment pipeline

---

## Next Step

After defining this structure:

- Begin implementing components step-by-step:
  1. UI
  2. Nodes
  3. LLM configuration
  4. State management
  5. Graph construction
  6. Integration through main.py

---
 
 
 # Frontend — UI (Streamlit)

- This section documents the frontend part of the project. 
- It explains purpose, responsibilities, files, and technical definitions for the Streamlit-based UI module used to drive the Agentic AI chatbot workflow.

## Overview

- The frontend is implemented using Streamlit and provides the user-facing controls to:
- select LLMs and model variants

- provide API keys
- choose use cases (Basic Chatbot, Chatbot with Tools, AI News)
- enter chat messages

- The UI triggers the backend workflow (LangGraph) by calling the modular pipeline from the selected configuration. The frontend is intentionally modular — split into configuration, loader, and display components — so the UI can be easily extended and maintained.

## Frontend Goals / Responsibilities

- Render control panel (left sidebar) containing:
        - LLM selection
        - Model selection for chosen LLM
        - API key input
        - Use-case selection
- Expose a chat/message input area
- Load constants and options from a configuration file
- Persist small UI state in session state
- Trigger workflow execution (via main.py / app.py)

## Files (UI module)

- Place all UI files under src/.../ui/streamlit/ 

- ui_config.ini — configuration file containing constants used by the UI (page title, LM options, use-case options, model lists).

- ui_config_file.py — module that reads ui_config.ini using ConfigParser and exposes getter methods (get_lm_options, get_usecase_options, get_grok_model_options, get_page_title, etc.).

- load_ui.py — contains LoadStreamlitUI class which:

        - loads configuration via Config
        - builds the Streamlit sidebar controls
        - returns a dictionary of `user_controls` (selected LLM, model, API key, use case, etc.)

- display_result.py — module responsible for rendering results / responses in the UI (kept separate to keep responsibilities modular).

- main.py — imports and uses the LoadStreamlitUI to build the UI and handle user input (connects sidebar selection → workflow trigger).

- app.py — application entry point; calls the function in main.py to start the Streamlit app.


## How the UI triggers the pipeline (brief flow)

- User selects options (LLM, model, use case) and provides API key in sidebar.
- LoadStreamlitUI returns user_controls to main.py.
- main.py shows the user message input box (Streamlit text input).
- When the user enters a message and submits:
        - `main.py` will validate required selections (e.g., API key for grok).
        - The app loads the selected LLM adapter (the LLM is configured via llms/ module, not detailed here).
        - main.py triggers the LangGraph workflow by passing the message + user_controls into the graph orchestration layer.
- The graph (nodes + edges + state) executes and returns a response.
- `display_result.py` formats and renders the response in the page.


## Implementation Guidelines

- Keep the UI modular: separate configuration, loader and renderer.
- Store all constants in ui_config.ini to avoid hard-coding values in the UI.
- Use ConfigParser for reading .ini file.
- Use select boxes for options that come from configuration (comma-separated lists).
- Persist sensitive values like API keys in st.session_state for the running session.
- Keep frontend responsibilities to UI rendering / capturing selections; backend orchestration lives in main.py and graph modules.

-----------------------------------------------

# LLM Model Integration — Grok (LangChain)

## Overview

This module is responsible for loading the selected LLM dynamically based on the **user inputs captured from the Streamlit frontend**.

The frontend collects:
- Selected LLM
- Selected model
- API key

These values are stored inside `user_controls` and passed to the LLM loader module.

This module reads those controls and initializes the corresponding LLM instance using `langchain_groq`.

---

# Objective

- Read API key from Streamlit user controls
- Read selected model from user controls
- Validate API key availability
- Initialize the Grok LLM using LangChain
- Return the LLM instance for workflow execution

---

# File Structure
LLMs/
└── groqllm.py

This file contains the class responsible for loading Groq LLM.

---

# Dependencies

The following libraries are required:

```python
import os
import streamlit as st
from langchain_groq import ChatGroq
```

- `os` → Used for environment variable handling
- `streamlit` → Used to access user controls and show errors
- `ChatGroq` → LangChain wrapper for Grok LLM

- User controls are created in: `ui/streamlit/load_ui.py`
- They include: `{ "grok_api_key": "...", "selected_grok_model": "...", ...}`
        - These controls are passed to the LLM loader class as input.

## Class Design
- Class: `GroqLLM`
- Encapsulates Grok LLM loading logic in a modular way.

## Model Loading Method
- Method: `get_llm_model()`
- Loads the Grok LLM based on:
        - API key
        - Selected model
- `if groq_api_key=='' and os.environ("GROQ_API_KEY") == '':` Why `and` condition:
- "API key must be provided via UI OR it must exist as environment variable"

| UI Key       | ENV Key      | Condition Result | Behavior  |
| ------------ | ------------ | ---------------- | --------- |
| Provided     | Not Provided | ❌ False          | ✅ Allowed |
| Not Provided | Provided     | ❌ False          | ✅ Allowed |
| Provided     | Provided     | ❌ False          | ✅ Allowed |
| Not Provided | Not Provided | ✅ True           | ❌ Error   |


-------------------------------------------------------------------