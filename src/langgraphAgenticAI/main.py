import streamlit as st
from src.langgraphAgenticAI.ui.streamlitUI.loadUI import LoadStreamlitUI
from src.langgraphAgenticAI.LLMs.groqllm import GroqLLM
from src.langgraphAgenticAI.graph.graph_builder import GraphBuilder
from src.langgraphAgenticAI.ui.streamlitUI.displayResults import DisplayResultStreamlit

def load_main():
    ## Starting point of the langraphAgenticAI project

    ui = LoadStreamlitUI()
    user_inputs = ui.load_streamlit_ui()

    if not user_inputs:
        st.error("Error : Failed to load user input.")
        return
    
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            obj_llm = GroqLLM(user_controls_input=user_inputs)
            model = obj_llm.get_llm_model()

            if not model:
                st.error("Error: LLM model cannot be initialized")   
                return

            # Initialize and set up the graph based on use case
            usecase = user_inputs.get('selected_usecase')
            if not usecase:
                st.error("Error: No use case selected.")
                return   
            
            #Graph Builder

            graphbuilder = GraphBuilder(model)
            try:
                graph = graphbuilder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()



            except Exception as e:
                st.error(f"Error: Graph setup failed - {e}")
                return

        except Exception as e:
            raise ValueError(f"Exception : {e}")
            

