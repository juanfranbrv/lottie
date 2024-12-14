import time
import json
import streamlit as st
from streamlit_lottie import st_lottie, st_lottie_spinner

st.set_page_config(
    page_title="Prueba de animaciones Lottie",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="auto"
)

st.header(f"Prueba de animaciones Lottie")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


columna_izquierda, columna_derecha = st.columns(2)


with columna_izquierda:

    lottie_animation_izq = load_lottiefile("./Animation - 1734201788003.json")
    st_lottie(lottie_animation_izq, speed=1, height=200,
              key="lottie",  loop=True)

with columna_derecha:

    lottie_animation_der = load_lottiefile(
        "./Animation - 1734202264690.json")
    with st_lottie_spinner(lottie_animation_der, height=100, key="spinner"):
        time.sleep(5)
    st.success("!! Proceso comletado ¡¡")
