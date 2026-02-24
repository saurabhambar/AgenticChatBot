import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """

        Load and run the LangGraph AgenticAI application with Streamlit UI.
        This function initializes the UI, handle user input, configures the LLM Model,
        set up the graph based on the selected use case, and display the output while 
        implementing excetpion handling for robustness.

    """
    ## Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from UI.")
        return
    
    user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            # Config LLM
            obj_llm_config = GroqLLM(user_control_input = user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized.")
                return
            
            # Initialize and setup the graph based on use case
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("Error: No use case selected.")
                return
        except:
            return