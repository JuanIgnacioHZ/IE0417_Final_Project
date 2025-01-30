import streamlit as st
from PIL import Image
import datetime as dt
import os
import pandas as pd
import plotly.express as px
import sys

sys.path.append("/app/dependencies")

from DB import obtener_elementos


st.set_page_config(layout='wide')

st.title("Dashboard")

col1, col2 = st.columns(2)

tabla = pd.DataFrame(
    obtener_elementos()
)

try:
    tabla['Fecha'] = pd.to_datetime(tabla['Fecha']).dt.date

    with col1:
        st.header('Gastos hasta la fecha')
        st.table(tabla)

    with col2:
        st.header('Emisores de los gastos')
        tabla_pie = tabla[['Emisor', 'Monto']].groupby('Emisor').sum().reset_index()
        pie_chart = px.pie(tabla_pie, values='Monto', names='Emisor')
        st.plotly_chart(pie_chart)

    st.header('Línea del tiempo con los gastos')
    tabla_tl = tabla[['Fecha', 'Monto']].groupby('Fecha').sum().reset_index()
    line = px.line(tabla_tl, x='Fecha', y='Monto')
    st.plotly_chart(line, use_container_width=True)

    st.header('Descarga de archivos')

    st.write('Elija el período de tiempo a descargar')

    col3, col4 = st.columns(2)

    with col3:
        startdate = st.date_input('Fecha de inicio')

    with col4:
        enddate = st.date_input('Fecha de fin')

    csv = tabla[tabla['Fecha'] >= startdate]
    csv = tabla[tabla['Fecha'] <= enddate]
    csv = csv.to_csv().encode('utf-8')

    st.download_button(
        label='Descargar CSV',
        data=csv,
        file_name=f"archivo.csv",
        mime='text/csv'
    )

    x = 5
except KeyError:
    st.header("En este momento no hay datos para mostrar, favor cargar facturas en la página de [subidas](Subida)")
