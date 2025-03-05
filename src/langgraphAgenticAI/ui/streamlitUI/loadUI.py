import streamlit as st
import os
import datetime as date

from langchain_core.messages import AIMessage, HumanMessage
from src.langgraphAgenticAI.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __inti__(self):
        self.config = Config()
        self.user_controls = {}
