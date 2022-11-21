# étant donné que le modèle est au format pickle
import pickle

# j'aurais besoin de tableau numpy pour les passer à mon modèle
import numpy as np
import streamlit as st
import inspect
from keras.models import load_model  # type: ignore
import tensorflow as tf  # type:ignore


# fonction qui fera la prédiction
# et qui reçoit un seul paramètre: les données d'entrées
# à l'intérieur de ce paramètre, il me faut
# --  # has_history, is_married, amount
def make_prediction1(data):
    # préchargement du modèle
    model = pickle.load(open("./model.pkl", "rb"))
    # passer les données d'entrée à notre modèle
    prediction = model.predict(data)

    # je n'ai pas trouvé l'intérêt de cette ligne
    # output = round(prediction[0], 2)

    # récupérer la prédiction
    output = prediction[0]
    return output


# fonction qui affiche un joli message
def print_result(pred):
    # plutot que d'afficher 0, afficher "credit non accordé"
    if pred == 0:
        print("\ncredit non accordé\n")
    # plutot que d'afficher 1, afficher "credit accordé"
    if pred == 1:
        print("\ncredit accordé\n")


def show_code(demo):
    """Showing the code of the demo."""
    show_code = st.sidebar.checkbox("Show code", True)
    if show_code:
        # Showing the code of the demo.
        st.markdown("## Code ayant permis de faire la prédiction")
        # get all the lines of the function
        sourcelines, _ = inspect.getsourcelines(demo)
        # show the lines of code
        st.code(("".join(sourcelines)))


# cette fonction attend 2 paramètres
# un chemin vers une image et un chemin vers un modèle de ML/DL
def make_prediction2(img, mdl="cat_dog_model.h5"):
    # je précharge mon modèle
    model = load_model(mdl)

    # config pour annoncer la taille de mon image
    image_size = (180, 180)

    # demander à keras de récupérer l'image que je lui donne en paramètre
    loaded_image = tf.keras.utils.load_img(img, target_size=image_size)
    # et transformer cette image sous forme de tableau
    img_array = tf.keras.preprocessing.image.img_to_array(loaded_image)
    # expand_dims ????
    img_array = tf.expand_dims(img_array, 0)

    # j'effectue une prédiction
    # je donne l'image à mon modèle
    # et ce dernier va me renvoyer la prédiction
    predictions = model.predict(img_array)

    score = predictions[0]
    rslts = (
        f"This image is {(score)*100} percent cat and {(1 - score)*100} percent dog."
    )
    # rslts = (score*100, (1 - score)*100)
    return rslts
