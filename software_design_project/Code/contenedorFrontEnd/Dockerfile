FROM python:3.8

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . /app

# Instala las dependencias necesarias
RUN apt-get update && apt-get install -y

# Instala las dependencias de Python
RUN pip install streamlit plotly pymongo

# Crea los directorios para subida de imágenes
RUN mkdir -p /img/photo_source
RUN mkdir -p /img/processed_photos

# Expone el puerto de la aplicación
EXPOSE 8502

# Ejecuta la aplicación
CMD streamlit run Home.py

