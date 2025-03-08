from langgraph.graph import StateGraph, START, END, MessagesState
from src.langgraphAgenticAI.state.state import State
from src.langgraphAgenticAI.nodes.node import Node
import streamlit as st

class GraphBuilder:

    def __init__(self, model):
        self.llm = model
        self.builder = StateGraph(State)


    def build_graph(self):
        '''Builds a basic chatbot using langgraph'''
        self.llm_node = Node(self.llm)
        self.builder.add_node("chatbot",self.llm_node.invoke_chatbot)
        self.builder.add_edge(START,"chatbot")
        self.builder.add_edge("chatbot",END)

    def setup_graph(self, usecase:str):    
        if usecase == "Basic Chatbot":
            self.build_graph()
        return self.builder.compile()

