import streamlit as st
import requests

st.title(
    "AI Notes Assistant"
)

question = st.text_input(
    "Ask your notes"
)

if st.button("Ask"):

    response = requests.post(

        "http://127.0.0.1:8000/ask",

        json={
            "question": question
        }
    )

    st.write(
        response.json()["answer"]
    )