import streamlit as st
import os
import datetime as date

from langchain_core.messages import AIMessage, HumanMessage
from src.langgraphAgenticAI.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def initialize_session(self):
        return {
            "current_step": "requirements",
            "requirements": "",
            "user_stories": "",
            "po_feedback": "",
            "generated_code": "",
            "review_feedback": "",
            "decision": None
        }
    

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.header(self.config.get_page_title())
        st.session_state.IsFetchButtonClicked = False
        st.session_state.timeframe = ''
        
        with st.sidebar:
            # Get Options from Config
            llm_options = self.config.get_llm_options()
            usercase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls['selected_llm'] == "Groq":
                # Model selection
                model_options = self.config.get_groq_model_options()

                self.user_controls["selected_groq_model"] = st.selectbox("Select Model",model_options)

                # API key
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key",type="password")

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter the GROQ API KEY to proceed.")

            self.user_controls["selected_usecase"] = st.selectbox("Select UseCase", usercase_options)

        if "state" not in st.session_state:
            st.session_state.state = self.initialize_session()

        return self.user_controls
        
        





