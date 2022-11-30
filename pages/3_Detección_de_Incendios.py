import streamlit as st
from findFireInImage import findFireInImage
from imageUtilities import decode_image, convertRasterToRGB, convertRasterToRealRGB
import tifffile

OUTPUT_PATH = './outputImage'
WEIGHTS_FILE = './weights/model_unet_Intersection_final_weights.h5'

def segmentacion_semantica():
    if 'images' not in st.session_state:
        st.session_state['images'] = dict()
        st.session_state['model'] = None
        st.session_state['img_counter'] = 0

    st.write("## Detección de incendios en imágenes satelitales - Segmentación semántica")

    if not st.session_state['images']:
        st.markdown(
        """
        Este módulo realiza la segmentación semántica de una imágen satelital para detectar los píxeles con un incendio forestal activo usando el modelo UNet preentrenado.

        Una vez procesada la imagen, se muestra la máscara con el resultado del procesamiento, siendo los píxeles en blanco aquellos con incendio presente.

        Se muestran también las bandas SWIR-Blue y RGB de la imágen para una fácil visualización de esta, dado que las imágenes satelitales no son directamente visibles ya que cuentan con más de 3 canales. Nótese que en las bandas SWIR-Blue es más fácil identificar el incendio forestal, por eso la literatura muestra que son una entrada adecuada para los modelos de detección de incendios.
        """)
        st.write("#### Cargue de imágen satelital")
        uploades_files = st.file_uploader("Sube una Imagen Satelital",  type = ['tif'], accept_multiple_files=True)
        if st.button("Detectar Incendios"):
            placeholder = st.empty()
            with placeholder.container():
                st.write("Convirtiendo las Imágenes")
                my_bar = st.progress(0)
                for i, uploaded_file in enumerate(uploades_files):
                    # To read file as bytes:
                    bytes_data = uploaded_file.getvalue()
                    name = uploaded_file.name
                    st.session_state['images'][name] = decode_image(bytes_data, name)
                    percent_complete = (i+1)/len(uploades_files)
                    my_bar.progress(percent_complete)
            
            placeholder.empty()
            st.experimental_rerun()
    else:
        if st.button("Reiniciar"):
            st.session_state['images'] = dict()
            st.session_state['img_counter'] = 0
            st.experimental_rerun()
        if len(st.session_state['images'].keys()) > 0:
            st.subheader("Análisis de incendios en imágen satelital")
            st.session_state['img_counter'] = 0
            col1, col2, col3 = st.columns(3)
        for name, path in st.session_state['images'].items():
            st.session_state['img_counter'] += 1
            image = tifffile.imread(path)
            out_image = findFireInImage(name,image,OUTPUT_PATH,WEIGHTS_FILE)
            with col1:
                if st.session_state['img_counter'] == 1:
                    st.write('#### Píxeles con Incendio Detectado')
                st.markdown('**Imágen {}**'.format(st.session_state['img_counter']))
                st.image(out_image)
            color_image = convertRasterToRGB(image)
            with col2:
                if st.session_state['img_counter'] == 1:
                    st.write('#### Imágen satelital en SWIR-Blue')
                st.markdown('**Imágen {}**'.format(st.session_state['img_counter']))
                st.image(color_image)
            real_RGB_image = convertRasterToRealRGB(image)
            with col3:
                if st.session_state['img_counter'] == 1:
                    st.write('#### Imágen satelital en RGB')
                st.markdown('**Imágen {}**'.format(st.session_state['img_counter']))
                st.image(real_RGB_image)
st.set_page_config(page_title="Segmentacion Semantica", page_icon="🔥")
segmentacion_semantica()
