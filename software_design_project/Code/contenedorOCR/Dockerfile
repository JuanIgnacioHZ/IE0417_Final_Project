FROM python:3.8

# Establece el directorio de trabajo
WORKDIR /app-OCR

# Copia los archivos de la aplicación al contenedor
COPY . /app-OCR

# Instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto de la aplicación
EXPOSE 5000

# Ejecuta la aplicación
CMD python3 -u app.py

