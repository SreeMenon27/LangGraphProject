import streamlit as st

with st.sidebar:
    llms = ["Groq","OpenAI"]
    selected_llm = st.selectbox("Select LLM",llms)

    if selected_llm == "Groq":
        st.text_area("value","You selected Groq")
        st.session_state.sel = "Groq"
    else:
        st.text_area("value","You selected OpenAI")
        st.session_state.sel = "OpenAI"

    st.text(st.session_state.sel)

st.markdown("<h1 style='text-align: center;'>🤖 LangGraph: Build Stateful Agentic AI graph</h1>")