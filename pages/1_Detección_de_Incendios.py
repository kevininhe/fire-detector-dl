import streamlit as st
from findFireInImage import findFireInImage
from imageUtilities import decode_image, convertRasterToRGB
import tifffile

OUTPUT_PATH = './outputImage'
WEIGHTS_FILE = './weights/model_unet_Intersection_final_weights.h5'

def segmentacion_semantica():
    if 'images' not in st.session_state:
        st.session_state['images'] = list()
        st.session_state['model'] = None

    if 'names' not in st.session_state:
        st.session_state['names'] = list()


    if not st.session_state['images']:
        uploades_files = st.file_uploader("Sube una Imagen",  type = ['tif'], accept_multiple_files=True)
        if st.button("Analizar Imagenes"):
            placeholder = st.empty()
            with placeholder.container():
                st.write("Convirtiendo las Imágenes")
                my_bar = st.progress(0)
                for i, uploaded_file in enumerate(uploades_files):
                    # To read file as bytes:
                    bytes_data = uploaded_file.getvalue()
                    name = uploaded_file.name
                    st.session_state['images'].append(decode_image(bytes_data, name))
                    st.session_state['names'].append(name)
                    percent_complete = (i+1)/len(uploades_files)
                    my_bar.progress(percent_complete)
            
            placeholder.empty()
            st.experimental_rerun()
    else:
        if st.button("Reiniciar"):
            st.session_state['images'] = list()
            st.experimental_rerun()
        for path in st.session_state['images']:
            st.header("Análisis de incendios en imágen satelital")
            image = tifffile.imread(path)
            out_image = findFireInImage(st.session_state['names'][0],image,OUTPUT_PATH,WEIGHTS_FILE)
            st.subheader('Píxeles con Incendio')
            st.image(out_image)
            color_image = convertRasterToRGB(image)
            st.subheader('Imagen satelital en RGB')
            st.image(color_image)
st.set_page_config(page_title="Segmentacion Semantica", page_icon="🔥")
segmentacion_semantica()