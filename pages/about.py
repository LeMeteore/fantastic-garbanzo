import streamlit as st  #type:ignore

st.set_page_config(page_title="Page à propos", page_icon="🌍") # titre affiché dans l'onglet
st.markdown("# Page à propos")
st.sidebar.header("About page in the side panel")
st.write(
    """
    This page displays the about page
    Lorem ipsum dolor

    """
)
