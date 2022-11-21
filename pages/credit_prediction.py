import streamlit as st
import numpy as np
from utils import make_prediction1, show_code

st.set_page_config(page_title="Predict page Foobar", page_icon="🌍")

st.sidebar.header("Credit prediction page")
st.sidebar.markdown("# Predict page foo bar baz 🎈")  # title inside margin
st.sidebar.write("I can write text inside the side bar too")

st.markdown("### Predict page XXXX")

st.write(
    """
    This page displays a form.\n
    Insert some data inside the form.\n
    Please press submit to make a prediction
"""
)

# https://docs.streamlit.io/library/api-reference/control-flow/st.form

with st.form("my_form"):
    st.write("Inside the form")

    # historyy = st.number_input(label="Do you have an history ? [0/1] ")
    married1 = st.number_input(label="Are you married ? [0/1] ")
    amount1 = st.number_input(label="What is the desired amount ? ")
    # history = st.checkbox("Do you have an history ?")
    # married = st.checkbox("Are you married ?")
    # amount = st.number_input(label="What is the desired amount ? ")

    # Every form must have a submit button.
    submitted = st.form_submit_button(label="Submit")

    # the form is submitted,
    if submitted:
        # récupérer toutes les champs du formulaire
        # convertir ces champs en nombres entiers
        int_features = [int(x) for x in (history, married, amount)]

        # transformation sous forme de tableau numpy
        final_features = [np.array(int_features)]

        # effectuer une prediction à l'aide la fonction définie plut tôt
        prediction = make_prediction1(final_features)

        st.write(f"With the values you submitted, the prediction is: {prediction}")

# show the code doing the prediction
show_code(make_prediction1)
