import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title('Facturas de Ticoburguesas')


st.markdown('Esta aplicación es un prototipo de un lector de vouchers, consta de dos páginas:')
st.markdown('   - Subida: permite cargar imágenes de los vouchers a analizar.')
st.markdown('   - Dashboard: pantalla de información de los datos ingresados, provee un resumen estadístico y facilita descargar los valores mostrados por rango de fechas.')
st.markdown('---')
st.markdown('Fue desarrollado como proyecto del curso IE0417 en el I semestre de 2023')
st.markdown('   - Profesor: Francisco Rojas')
st.markdown('Integrantes:')
st.markdown('   - Francisco Leal Tovar')
st.markdown('   - Javier Acosta Villalobos')
st.markdown('   - Juan Ignacio Hernández Zamora')

x = 1
