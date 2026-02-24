import streamlit as st
import os
from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI():
    def __init__(self):
        self.config = Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(),layout="wide")
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:
            llm_option = self.config.get_llm_option()
            usecase_options = self.config.get_usecase_option()

            # LLM Option
            self.user_controls["selected_llm"] = st.selectbox("Select LLM",llm_option)

            if self.user_controls["selected_llm"] == "Groq":
                # Model Selection
                model_option = self.config.get_groq_model_option()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_option)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning(" ⚠️ Please enter your GROQ API key to proceed. Don't have? refer: https://console.groq.com/keys ")

            # UseCase Selection 
            self.user_controls["selected_usecases"] = st.selectbox("Select Usecases", usecase_options)
        
        return self.user_controls