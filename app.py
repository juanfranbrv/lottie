import time
import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie, st_lottie_spinner

st.set_page_config(
    page_title="Prueba de animaciones Lottie",
    page_icon="🤖",
    # layout="wide",
    initial_sidebar_state="auto"
)

st.header(f"Prueba de animaciones Lottie")
st.markdown('''Lottie es una biblioteca de código abierto desarrollada por Airbnb que permite crear animaciones vectoriales de alta calidad en tiempo real.
Sus principales caracteristicas son:

- **Escalabilidad**: Animaciones vectoriales que no pierden calidad al adaptarse a diferentes pantallas.
- **Ligereza**: Archivos JSON más pequeños que videos o GIFs.
- **Interactividad**: Control total sobre la reproducción (pausar, reiniciar, cambiar velocidad, etc.).
- **Multiplataforma**: Compatible con web, iOS, Android y más.
- **Fácil creación**: Exportación directa desde After Effects con el plugin Bodymovin.


''')


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.subheader("Puede trabajarse con ficheros locales:")
columna_izquierda, columna_derecha = st.columns(2)

with columna_izquierda:

    lottie_animation_izq = load_lottiefile("./Streamlit Logo Animation.json")
    st_lottie(lottie_animation_izq, speed=1, height=200,
              key="lottie",  loop=True)

with columna_derecha:

    if st.button("Pulsa para iniciar un calculo bastante largo"):

        lottie_animation_der = load_lottiefile(
            "./Animation - 1734202264690.json")
        with st_lottie_spinner(lottie_animation_der, height=100, key="spinner"):
            time.sleep(10)
        st.success("!! Proceso comletado ¡¡")

st.subheader("Puede trabajarse con fichero desde la red:")
columna_izquierda, columna_derecha = st.columns(2)

with columna_izquierda:
    lottie_animation_izq2 = load_lottie_url(
        "https://lottie.host/e9ce5dce-f70f-424f-a4a0-4f3aaed462b6/tekDr82cX8.json")
    st_lottie(lottie_animation_izq2, speed=1, height=200,
              key="lottieiz2",  loop=True)

with columna_derecha:
    url = st.text_input("Escribe la URL de un fichero Lottie")
    if url:
        lottie_animation_der2 = load_lottie_url(url)
        st_lottie(lottie_animation_der2, speed=1, height=200,
                  key="lottiede2",  loop=True)
