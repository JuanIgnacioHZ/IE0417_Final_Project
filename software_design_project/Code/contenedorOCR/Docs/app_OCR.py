import pytesseract
import re
import glob

from PIL import Image

# Ruta de la carpeta que contiene las imagenes
carpeta_imagenes = '/entradaOCR'

# Obten la lista de nombres de archivo de las imagenes en la carpeta
extensiones_permitidas = ['*.jpg', '*.jpeg', '*.png']  # Puedes ajustar las extensiones segun tus necesidades
archivos_imagen = []
for extension in extensiones_permitidas:
    archivos_imagen.extend(glob.glob(f"{carpeta_imagenes}/{extension}"))

# Procesa cada imagen
for imagen in archivos_imagen:
    imagen_pil = Image.open(imagen)

    # Obtiene el texto de la imagen a color
    text = pytesseract.image_to_string(imagen_pil)
    
    print(f"Texto en {imagen}:")
    #print(text)

    # Patron para obtener por ejemplo "CRC 10.000" 
    pattern = r"CRC (\d{1,3}\.\d{3})"



    # Busca el patron en el texto de la imagen
    result = re.search(pattern, text)

    if result:
        number = result.group(1)
        print(number)

    # Buscar patron en imagen en escala de grises
    else:
        ### Convierte la imagen a escala de grises para mejorar el rendimiento del OCR
        gray_image = imagen_pil.convert("L")
    
        # Obtiene el texto de la imagen en escala de grises
        text = pytesseract.image_to_string(gray_image)
        
        # Busca el patron en el texto de la imagen
        result = re.search(pattern, text)

        if result:
            number = result.group(1)
            print(number)



    #parte_entera = int(number.replace(".", ""))
            

print('Aeny;ladsfj')
