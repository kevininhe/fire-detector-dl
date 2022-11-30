import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import cv2

LOGGER = get_logger(__name__)

def planteamiento_modelo():
    st.set_page_config(
        page_title="Planteamiento Modelo"
    )

    st.write("# Planteamiento del modelo - Estado del arte")

    st.markdown(
        """
        A continuación se explicarán las partes más importantes del modelo preentrenado (UNet), además de varias mejoras que se han realizado en trabajos recientes sobre detección de incendios.
        #### Vista general del modelo preentrenado - Estado del arte
        """
    )
    img = cv2.imread('./model/Arquitectura_DL_Fire.jpg', cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    st.image(img)
    st.markdown(
        """
        En la imagen anterior se muestra la arquitectura de un modelo UNet, el cual se está utilizando en este aplicativo, junto con varias mejoras que se han planteado en los trabajos más recientes.
        #### Componentes principales
        **Entrada del modelo**
        
        Una de las dificultades principales que impedían el uso de técnicas de Deep Learning para el análisis de imágenes satelitales era la falta de un set de datos anotado sobre el cual se pudiera realizar el entrenamiento de esta clase de modelos. Sin embargo, gracias al trabajo realizado en 2021 en Pereira et. al [1], donde los autores analizaron una gran cantidad de imágenes del satélite Landsat 8 en búsqueda de incendios activos, ahora se cuenta con un set con imágenes de incendios forestales en los 5 continentes, gracias a lo cual en los últimos 2 años han surgido varias propuestas para la segmentación semántica de este set de imágenes, identificando los píxeles en los cuales se detecta un incendio activo.

        Para crear el set de imágenes se dividieron las imágenes capturadas del satélite Landsat 8 en parches de tamaño 256 x 256 (que en el suelo representan 7680 x 7680 m) que tienen las 11 bandas de la imágen original excepto la banda Pancromática (banda 8).

        En Pereira et. al se encontró también que no es necesario usar las 10 bandas de la imágen satelital sino que los mejores resultados se obtienen usando principalmente las bandas SWIR (Shortwave Infrared, o Infrarrojo de onda corta), y la banda Blue (azul), por ende, la entrada al modelo es una imágen de tres bandas: dos SWIR, que son las bandas 6 y 7 de una imágen Landsat 8, y la banda Blue, que es la banda 2.

        Por ende, este aplicativo recibe como entrada un parche de tamaño 256 x 256 con 10 bandas, y antes de procesar la imágen se extraen las bandas 2, 6 y 7.

        **Max Pooling**

        El modelo aplica Max Pooling en el encoder para ir reduciendo el tamaño de la entrada a medida que esta pasa por las diferentes capas del modelo. Sin embargo, al igual que se reducen las dimensiones de la entrada se aumenta también la profundidad de esta. Esto permite obtener en las capas más profundas.

        **Convolucional Transpuesta + Upsampling**

        A medida que el código pasa por el decoder, sus dimensiones se deben aumentar ya que la salida del modelo debe tener las mismas dimensiones que la entrada. Esto se hace usando capas convolucionales transpuestas, las cuales se pueden ver como una "inversa" de aplicar una convolución con stride. Esto permite hacer el "upsampling" del código, incrementando sus dimensiones a medida que pasa por las capas del decoder, hasta llegar al tamaño de la entrada.

        **Concatenar**

        Concepto típico de la arquitectura Unet, la salida de las diferentes capas del encoder se usa como una entrada adicional de las capas del decoder que tengan el mismo tamaño, esto para evitar el problema de desvanecimiento del gradiente.

        **Softmax**

        Ya que en este modelo la detección de incendios forestales en imágenes satelitales se planteó como un problema de segmentación semántica, donde se deben identificar los píxeles con incendios activos, la salida del modelo es una máscara con píxeles cuyos valores solamente son 1 si se detectó un incendio forestal en ellos o 0 si no tienen incendio forestal. La función Softmax permite obtener valores entre 1 y 0, y junto con la función de costo de entropía cruzada binaria, permiten obtener una matriz de valores entre 1 y 0, cada uno correspondiente a la probabilidad de que un píxel tenga un incendio forestal, y esta salida se grafica para poder identificar visualmente los píxeles donde el modelo detectó un incendio.
        
        #### Mejoras planteadas en trabajos recientes

        **Tamaño variable del Kernel**

        En el trabajo de Rostami et.al [2] se encontró que el uso de kernels convolucionales de tamaños diferentes en forma simultanea permite hacer una mejor clasificación que con un modelo UNet simple, principalmente al clasificar píxeles aislados con incendios forestales.

        **Kernels convolucionales con Dilatación**

        En Rostami et.al se encontró también que el uso de Kernels convolucionales con dilatación permite identificar de mejor manera los píxeles de incendios en incendios de escala múltiple aún cuando el tamaño de la imágen varia. La dilatación en los kernels convolucionales se maneja con un hiperparámetro llamado "tasa de dilatación", el cual amplía el campo de visión de un Kernel pero hace que ignore todo aquello que está fuera de su tamaño original. Por ejemplo, un Kernel 3 x 3 con tasa de dilatación 2 tiene el mismo campo de visión que un Kernel 5 x 5.
        
        **Profundidad de la UNet**
        
        En Rostami et.al se encontró que usar 5 capas convolucionales daba un mejor resultado que usar 3 capas convolucionales, que es lo planteado en el modelo UNet, esto por supuesto combinandolo con técnicas de variación del tamaño del kernel y el uso de Kernels convolucionales con dilatación.
        
        **Segmentación no supervisada usando la banda "cirrus cloud"**

        En Sun et.al [3] se encontró que al hacer una clasificación no supervisada de la banda 9 (cirrus cloud) de las imágenes satelitales usando K-means y agregando esta entrada al modelo, se logra aumentar la velocidad y estabilidad del entrenamiento del modelo, permitiendo construir un modelo más simple que requiere de menos recursos computacionales. Esto implica que hay cierta relación entre la nubosidad del terreno y los incendios forestales.
        
        [1]: <https://www.sciencedirect.com/science/article/abs/pii/S092427162100160X?via%3Dihub>
        [2]: <https://www.mdpi.com/2072-4292/14/4/992>
        [3]: <https://arxiv.org/pdf/2201.09671.pdf>
        """
    )
planteamiento_modelo()
