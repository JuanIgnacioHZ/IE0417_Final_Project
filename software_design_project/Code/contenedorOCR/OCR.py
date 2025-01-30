import pytesseract
import re
import glob
from string import ascii_letters
from PIL import Image

def obtener_diccionario(texto_vouch):
    '''
        Esta función recibe el texto de un voucher escaneado
    mediante tesseract, busca el total, la fecha, quién lo
    emitió y devuelve la información en formato lista
    '''

    # Declaración de constantes:
    # Patrones para reconocer fecha, monto y emisor
    total_regex = r"(\d{1,3},\d{3}.\d{2})|CRC\s\w{0,1}(\d{1,3}.\d{3})|\w{3,5}\s\w{0,1}(\d{1,3}, \d{3})"
    fecha_regex = r"(\w{3}\s\d{2} \d{4})|(\w{3} \d{2}\S\s\d{2})|(\w{3} \d{2},\d{4})"
    emisor_regex = r"TERMINAL|TERM|ERM"

    # Vectores para obtener total y fecha
    patrones_re = [total_regex, fecha_regex]
    salida = []

    # Nombres de meses para enviarlos numéricamente
    meses = ["enero",
             "febrero",
             "marzo",
             "abril",
             "mayo",
             "junio",
             "julio",
             "agosto",
             "setiembre",
             "octubre",
             "noviembre",
             "diciembre"]

    # Empieza por buscar los datos deseados en el texto
    # leído del voucher
    for i in range(len(patrones_re)):
        resultado = re.search(patrones_re[i], texto_vouch)
        if (resultado is not None):
            salida.append(resultado.group())
        else:
            return None

    # Con el total y la fecha, se puede obtener quién emitió
    # el vouhcer
    texto_vouch = texto_vouch.split("\n")
    texto_vouch = [elemento for elemento in texto_vouch if elemento != ""] # Elimina caracteres inválidos
    for i in range(len(texto_vouch)):
        # Se evalúan el texto_voucho obtenido por renglones
        # hasta obtener algo similar a: "TRAMITAR SOLO EN"
        # El emisornte de la transacción se toma como la 
        # concatenación de los dos renglones inmediatamente
        # anteriores a este
        if (re.search(emisor_regex, texto_vouch[i]) is not None):
            str_tmp = (texto_vouch[i-3] + ", " + texto_vouch[i-2]).replace("\n", "")
            str_tmp = str_tmp.title()
            salida.append(str_tmp) 

    # Teniendo los datos crudos, se convierte la fecha al formato DD-MM-AAAA
    salida[1] = salida[1].replace(",", " ")  # Se eliminan comas cuando aparezcan
    salida[1] = salida[1].replace("  ", " ")  # Se eliminan los dobles espacios
    salida[1] = salida[1].split(" ")

    # Se pasa del nombre del mes al número de 1 a 12
    mes_num = 0
    for i in range(len(meses)):
        if (salida[1][0].lower() in meses[i]):
            mes_num = i+1
  
    # Se corrige el rango de los años, de manera
    # que siemrpe sea 20xx
    if (len(salida[1][2]) == 2):
        salida[1][2] = "20" + salida[1][2]
    elif ((salida[1][2][0] + salida[1][2][1]) == "26"):
        # Es para el caso que confunde el 20xx con 26xx
        salida[1][2] = "20" + salida[1][2][2] + salida[1][2][3]

    # Formato final de la fecha tipo día-mes-año
    salida[1] = (salida[1][1] + '-' + str(mes_num) + '-' + salida[1][2])

    # Se corrige el formato para el monto total
    # Elimina las centésimas de colón
    if (salida[0][-3] == '.'):
        salida[0] = salida[0][0:-3]
    # Elimina caracteres alfanuméricos y espacios
    salida[0] = re.sub("\D", "", salida[0])
    salida[0] = salida[0].replace(" ", '')
    salida[0] = float(salida[0])

    # La información se devuelve como lista según el formato:
    # [Emisor(str), fecha(str), monto(float)]
    return [salida[2], salida[1], salida[0]]



def leer_voucher(archivo):
    '''
        Esta función recibe la dirección de la foto del voucher
    a procesar, la analiza en primera instancia con la imagen
    en escala de grises, y luego a color.
        Compara los resultados de ambos análisis y en caso de
    presentarse discrepancias toma la referencia en escala de grises
    '''
    # Empieza por leer la imagen
    imagen_pil = Image.open(archivo)

    ### Convierte la imagen a escala de grises para mejorar el rendimiento del OCR
    gray_image = imagen_pil.convert("L")

    # Obtiene el texto de la imagen en escala de grises
    texto_egrises = pytesseract.image_to_string(gray_image)

    # Llama a la función para obtener los datos relevantes
    salida = obtener_diccionario(texto_egrises)

    # Finalmente, devuelve los datos en formato de diccionario
    return {"Emisor":salida[0], "Fecha":salida[1], "Monto":salida[2]}

# Prueba
#imagen = 'Docs/VouchersE/Vouchers_proy_IE0417_6.jpg'
#print(leer_voucher(imagen))
