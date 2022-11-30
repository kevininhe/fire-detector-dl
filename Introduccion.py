import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Introduccion",
        page_icon="👋",
    )

    st.write("# Detección de incendios en imágenes satelitales usando Deep Learning")

    st.markdown(
        """
        Los incendios activos son desastres naturales devastadores que causan daños socioeconómicos en todo el mundo, por lo cual su oportuna detección se ha convertido en una tarea muy importante para el planeta y la humanidad.

        Las imágenes satelitales son un medio muy valioso para la detección de incendios dado su alcance global y a los datos que contienen, que van mucho más allá de una combinación de colores como en una imagen tradicional ya que abarcan un espectro de ondas mucho más amplio que el captado por el ojo humano. Dependiendo del satélite que capture la imágen, una imágen satelital puede contener información sobre la nubosidad del terreno, temperatura del suelo, entre otros datos, capturados gracias a las ondas de diferentes tipos de ondas captados por el satélite.

        Hasta el momento para la detección de incendios usando imágenes satelitales se han utilizado técnicas manuales orientadas a realizar operaciones matemáticas sobre las diferentes ondas captadas por el satélite, sin embargo, estas técnicas no consideran factores como la forma del incendio o la información que se podría obtener de otras bandas, por lo cual hay una gran oportunidad de mejora al usar técnicas de Deep Learning, caracterizadas por encontrar patrones que muchas veces no pueden ser detectados por un humano.

        En este aplicativo podrá interactuar con un modelo de Deep Learning preentrenado para la detección de incendios en imágenes satelitales.

        ### Secciones
        - **Planteamiento del modelo:** Descripción general del modelo preentrenado (UNet) y una breve introducción al estado del arte actual.
        - **Obtención imágenes satelitales:** Dada lo complejo que puede llegar a ser obtener imágenes satelitales, y más encontrar imágenes satelitales con incendios forestales activos, en esta sección se provee un módulo para la descarga de este tipo de imágenes.
        - **Detección de incendios**: Puede cargar una imágen satelital en formato .tif, tras lo cual se procesará por el modelo preentrenado y podrá visualizar los píxeles en los que se detectó un incendio activo.
    """
    )

if __name__ == "__main__":
    run()
