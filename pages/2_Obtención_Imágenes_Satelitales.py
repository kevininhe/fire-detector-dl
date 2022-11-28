import streamlit as st
from streamlit.logger import get_logger
import pandas as pd

LOGGER = get_logger(__name__)
LAT_LON_FILE = 'img_lat_lon.csv'


def obtencion_imagenes():
    st.set_page_config(
        page_title="Obtener Imágenes",
        page_icon="🏞️",
    )

    st.write("# Obtención de imágenes satelitales")

    st.markdown(
        """
        Dada la dificultad que representa el obtener imágenes satelitales, ya que a diferencia de las imágenes RGB estas no se pueden obtener directamente desde Google luego de dos clicks, se dispuso del siguiente [Set de Imágenes satelitales](https://drive.google.com/drive/folders/1W2HFUhyoqwzqWJYlgr_cs5dBBCNyFujG?usp=sharing) con incendios que los usuarios pueden usar para interactuar con el modelo.
        """
    )
    st.markdown(
        """
        #### ¿De qué lugares son las imágenes satelitales con incendios?
        En este mapa se muestran las ubicaciones aproximadas de las imágenes presentes en el set de datos
        """
    )
    df = pd.read_csv(LAT_LON_FILE)
    st.map(df,zoom=0)
obtencion_imagenes()