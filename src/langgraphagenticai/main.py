import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groq_llm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit 

def load_langgraph_agenticai_app():
    """

        Load and run the LangGraph AgenticAI application with Streamlit UI.
        This function initializes the UI, handle user input, configures the LLM Model,
        set up the graph based on the selected use case, and display the output while 
        implementing excetpion handling for robustness.

    """
    # 1. Load UI and collect user_controls
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()
    print(user_input)

    if not user_input:
        st.error("Error: Failed to load user input from UI.")
        return
    
    # 2. Wait for user message input (Streamlit chat_input)
    user_message = st.chat_input("Enter your message:")
    print(f"User Message: {user_message}")

    if user_message:
        try:
            # 3. Configure / initialize LLM using user_controls
            obj_llm_config = GroqLLM(user_control_input = user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized.")
                return
            
            # 4. Identify use case (e.g., "basic_chatbot")
            # Initialize and setup the graph based on use case
            usecase = user_input.get("selected_usecases")
            print(usecase)
            if not usecase:
                st.error("Error: No use case selected.")
                return
            
            # 5. Initialize GraphBuilder with the LLM
            graph_builder = GraphBuilder(model)
            try:
                 # Setup the required graph based on selected use case
                graph=graph_builder.setup_graph(usecase)
                # 6. Execute the graph with the user message as payload
                # 7. Render/display the result using UI Display class
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e: 
                st.error(f"Error: Graph setup Failed - {e}")
                return
            
        except Exception as e:
            st.error(f"Error: Graph setup Failed - {e}") 
            return