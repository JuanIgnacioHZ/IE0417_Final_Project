#!/usr/bin/python3
# Este script se encarga de leer un directorio de facturas de prueba
# y un directorio con información ya extraída de las facturas, ejecuta el
# código del OCR y da porcentajes de similitud
from OCR import leer_voucher
from difflib import SequenceMatcher
from os import system, popen

def obtener_imgs(dir_imgs):
    '''
    Esta función lee el directorio de vouchers de prueba y obtiene sus
    sus nombre en orden.
    '''
    print("Paso 1/4. Obtención de imágenes a procesar mediante el OCR.")
    # Lee el directorio
    cmd_imgs = 'ls "' + dir_imgs + '"'
    imgs = (popen(cmd_imgs, 'r').read()).split('\n')
    imgs.remove('')     # Elimina el caracter vació de la salida de la terminal

    # Agrega la ruta relativa respecto a la carpeta de validación
    for i in range(len(imgs)):
        imgs[i] = (dir_imgs + imgs[i])

    print("\tListo, ", len(imgs), 'imágenes detectadas.')

    return imgs


def procesar_imgs(imgs):
    '''
    Esta función corre el lector del OCR sobre las imágenes detectadas
    y devuelve una lista con los diccionarios resultantes
    '''
    print("Paso 2/4. Lectura en el OCR de las imágenes obtenidas.")
    salida = []
    for i in imgs:
        salida.append(leer_voucher(i))

    print("\tListo, se procesaron ", len(salida), 'imágenes.')

    return salida


def leer_datos(archivo_referencia):
    '''
    Esta función lee los datos de referencia de un archivo de valores esperados
    para el OCR
    '''
    print("Paso 3/4. Lectura de datos de referencia.")
    # Abre el archivo
    archivo = open(archivo_referencia, 'r')

    salida = []
    for i in archivo:
        # Del csv, elimina los datos innecesarios y crea el diccionario
        i = i.replace('\n', '')
        i = i.replace("','", ';')
        i = i.replace("'", '')
        i = i.split(';')
        i[2] = float(i[2])
        dic_tmp = {"Emisor":i[0], "Fecha":i[1], "Monto":i[2]}
        salida.append(dic_tmp)

    # Cierra el archivo
    archivo.close()

    print("\tListo, se obtuvieron ",  len(salida), 'valores de referencia.')

    # Devuelve los datos de referencia
    return salida


def comparar_datos(lista_referencia, lista_OCR):
    '''
    Esta función recibe dos listas de diccionarios ordenados,
    uno con la información de referencia que se espera del OCR,
    y otra la salida real del OCR, va de uno en uno comparando
    todos sus valores e imprime el grado de correlación que tienen
    '''
    print("Paso 4/4. Comparación de los datos obtenidos.")
    # Declaración de constante
    valores_a_comparar = ["Emisor", "Fecha", "Monto"]
    
    # En primer lugar, verifica que los datos sean comparables
    if len(lista_referencia) != len(lista_OCR):
        print("Error, los datos no son comparables.")
        # No devuelve nada
        return None

    # Si son comparables, los compara e imprime los datos
    for i in range(len(lista_referencia)):
        print("\tVerificando muestra ", i + 1, " de ", len(lista_referencia))
        print()
        print("\t\tDatos en estudio:")
        print("\t\t\tReferencia:\t ", lista_referencia[i])
        print("\t\t\tLectura OCR:\t ", lista_OCR[i])
        print()
        print("\t\tResultados:")
        print("\t\t{0}\t{1}".format("Argumento", "Correlación (%)"))
        for j in valores_a_comparar:
            corr_ratio = SequenceMatcher(None, str(lista_referencia[i][j]), str(lista_OCR[i][j])).ratio()
            print("\t\t{0}\t\t{1}%".format(j, corr_ratio*100))

    print("\tListo, todos los datos detectados fueron comparados.")

    # No devuelve nada
    return None

# Declaracón de variables
archivo_ref = "Datos_referencia.csv"
dir_imgs = "./Facturas de prueba/"
lista_OCR = (procesar_imgs(obtener_imgs(dir_imgs)))
lista_referencia = (leer_datos(archivo_ref))

# Inicio del programa

comparar_datos(lista_referencia, lista_OCR)

