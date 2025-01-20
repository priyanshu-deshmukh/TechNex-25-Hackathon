import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer

def main():


    st.set_page_config(
        page_title="Hello",
        page_icon="",
    )


    st.logo("images/logo.jpg")
    st.title("Krishi AI 🧑‍🌾")



    col1, col2, col3 = st.columns(3 )

    with col1:
        st.header("Predict")
        st.image("https://static.streamlit.io/examples/dog.jpg")
        st.link_button("Start Prediction", "http://localhost:8501/Predict")


    with col2:
        st.header("Suggestions")
        st.image("https://static.streamlit.io/examples/dog.jpg")
        st.button("Get Suggestions",  type="primary")

    with col3:
        st.header("Trends")
        st.image("https://static.streamlit.io/examples/dog.jpg")
        st.button("Current Trends",  type="primary")


if __name__ == '__main__':
    main()

