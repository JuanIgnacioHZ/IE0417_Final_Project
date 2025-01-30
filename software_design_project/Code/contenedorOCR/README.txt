# Crear un volumen
sudo docker volume create volumenOCRentrada

# Obtener info del volumen
sudo docker volume inspect volumenOCRentrada

# Copiar vouchers en el volumen... Revisar paths
# sudo cp ~/proyecto/proyecto-factura_de_ticoburguesas/Code/contenedorOCR/VouchersE/* /var/lib/docker/volumes/volumenOCRentrada/_data/.

# Construir el contenedor del programa python-OCR
sudo docker build -t python-ocr .

# Ejecutar el contenedor de python-OCR
sudo docker run -v volumenOCRentrada:/entradaOCR --name python-ocr python-ocr



# Borrar todos los contenedores
sudo docker rm -f $(docker ps -aq)

# Borrar el volumen
sudo docker volume rm volumenOCRentrada

