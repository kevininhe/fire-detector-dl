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

        Las imágenes satelitales son un medio muy valioso para la detección de incendios dado su alcance global y a los datos que contienen, que van mucho más allá de una combinación de colores como en una imagen tradicional. Dependiendo del satélite que capture la imágen, una imágen satelital puede contener información sobre la nubosidad del terreno, temperatura del suelo, entre otros datos, capturados gracias a las ondas de diferentes tipos que emite el satélite.

        La gran cantidad de imágenes satelitales existente y la gran cantidad de datos que guarda cada imágen hace de la detección de incendios en imágenes satelitales un problema complejo, por lo cual se requiere de técnicas avanzadas como el Deep Learning para poder obtener modelos que permitan identificar estos incendios con la mayor precisión posible.

        En este aplicativo podrá interactuar con el modelo de Deep Learning propuesto para la detección de incendios en imágenes satelitales.

        ### Secciones
        - **Planteamiento del modelo:** Descripción general del modelo construido.
        - **Obtención imágenes satelitales:** Dada lo complejo que puede llegar a ser obtener imágenes satelitales, y más encontrar imágenes satelitales con incendios forestales activos, en esta sección se provee un módulo para la descarga de este tipo de imágenes.
        - **Detección de incendios**: Puede cargar una imágen satelital en formato .tif, tras lo cual se procesará por el modelo propuesto y podrá visualizar los píxeles en los que se detectó un incendio activo.
    """
    )

if __name__ == "__main__":
    run()