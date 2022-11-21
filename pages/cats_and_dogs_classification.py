import pathlib
import streamlit as st
import numpy as np
from utils import make_prediction1, make_prediction2, show_code  # type:ignore

root_folder = pathlib.Path(__file__).parent.parent.resolve()  # current directory

st.set_page_config(page_title="Cat Dog prediction page")  # titre affiché dans l'onglet
st.sidebar.header("Prediction page for cats and dogs")  # titre affiché dans la marge

st.markdown("# Prediction page")  # titre affiché dans la page

st.write(
    """
    This page displays a form.\n
    Upload an image inside the form.\n
    Please press submit to make a prediction
"""
)

# https://docs.streamlit.io/library/api-reference/control-flow/st.form

with st.form("my_form"):
    # affichage formulaire
    uploaded_file = st.file_uploader("Choose a jpeg file containing a dog or a cat: ")
    submitted = st.form_submit_button(label="Submit")

    # is le bouton submit a été cliqué, il recevra la valeur vraie
    if submitted:
        if uploaded_file is not None:
            # where I want to save the file
            saved_file_path = root_folder / "uploads" / uploaded_file.name
            # save uploaded file somewhere
            with open(saved_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # display the uploaded image
            st.image(uploaded_file.getvalue())

            # make prediction and display prediction
            prediction = make_prediction2(saved_file_path)
            st.write(f"With the picture you submitted, the prediction is: {prediction}")
