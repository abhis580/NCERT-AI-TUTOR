import streamlit as st
from src.rag import create_rag_chain

@st.cache_resource
def load_rag():
    return create_rag_chain()

ragchain = load_rag()

st.title("😊 NCERT AI Tutor")

question = st.text_input("Please ask your question")

if st.button("Ask"):

    answer = ragchain.invoke(question)
    st.title("🙆🏼‍♂️")

    st.write(answer)