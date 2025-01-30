import streamlit as st
from PIL import Image
import datetime
import os

@st.cache_data
def load_image(image_file):
    img = Image.open(image_file)
    return img

st.set_page_config(
    page_title="Upload",
    page_icon="⬆️",
)

st.title('Facturas de Ticoburguesas')

st.header('En esta página puede subir facturas al sistema')

image = st.file_uploader('Subir imágenes (acepta imagenes .png, .jpeg y .jpg)', type=['png','jpeg','jpg'])



if image is not None:

    photo_source = (os.popen('echo $photo_source_dir', 'r').read().replace('\n', '').split(' '))[0] # /TODO Verificar esto

    file_details = {'FileName': image.name, 'FileType': image.type}
    # st.write(file_details)
    img = load_image(image)

    st.image(img)
    now = str(datetime.datetime.now().timestamp()).replace('.', '')
    type_string = str(image.type).replace('image/', '')
    if st.button('Guardar imagen'):
        with open(os.path.join(photo_source,f'{now}.{type_string}'),"wb") as f:
            f.write(image.getbuffer())
        st.success('Imagen guardada')
