from src.langgraphAgenticAI.state.state import State

class Node:

    def __init__(self,model):
        self.llm = model

    def invoke_chatbot(self, state:State) -> dict:
        return {"messages": self.llm.invoke(state["messages"])}
