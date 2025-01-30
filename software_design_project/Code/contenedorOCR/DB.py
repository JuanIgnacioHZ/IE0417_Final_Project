#!/usr/bin/python3

# Importa bibliotecas para acceder a Mongo
from pymongo import MongoClient, errors
from os import popen


def agregar_elemento_db(elemento):
    # Se conecta a la base de datos
    vouchers, ultimo_id = conectar_base()

    # Se obtiene el diccionario para el siguiente id
    datos = {'_id': (ultimo_id + 1)}

    # Y se crea el diccionario a agregar a la base
    datos.update(elemento)

    # Agrega el elemento indicado a la base
    vouchers.insert_one(datos)

    # Se informa del elemento agregado
    print("Voucher leído y agregado al la base de datos.\t", datos)


def conectar_base():

    # Obtiene los datos  de usuario de variables de entorno, para facilitar la configuración
    IP_mongo = (popen('echo $MONGO_IP_ADDR', 'r').read().replace('\n', '').split(' '))[0]
    usuario = (popen('echo $MONGO_INITDB_ROOT_USERNAME', 'r').read().replace('\n', '').split(' '))[0]
    contra = (popen('echo $MONGO_INITDB_ROOT_PASSWORD', 'r').read().replace('\n', '').split(' '))[0]

    # Se intenta conectar a la base, si algo fallara
    # se levante un error
    try:
        # Conección a la base
        cliente = MongoClient(
            host = [ IP_mongo + ":" + '27017' ],
            serverSelectionTimeoutMS = 3000, # 3 second timeout
            username = usuario,
            password = contra
            )

        # Si la conexión es exitosa, se imprime que se conectó y
        # la versión del servidor
        print("Conexión exitosa.")
        # print("Versión del servidor: ", cliente.server_info()["version"]) # No es necesario

        # Se obtiene la lista de bases de datos presentes
        bases_disponibles = cliente.list_database_names()

        # Se valida si existe o no la base de datos
        datos_contables = cliente["datos_contables"]

        # Análogamente, se hace lo mismo para la colección de 
        # datos que tiene los vouchers
        colecciones = datos_contables.list_collection_names()
        vouchers = datos_contables["vouchers"]


                # Llegado este punto, se verifica si todo está creado
        # al buscar un dato place holder y si no se encuentra
        # se agrega
        res_tmp = vouchers.find({})
        try:
            res_tmp = vouchers.insert_one({"_id":-1,
                                            'Emisor': None,
                                            'Fecha': None,
                                            'Monto': None})
        except errors.DuplicateKeyError:
            pass

        # Obtiene el id del último elemento para seguir
        # la secuencia
        ultimo_id = vouchers.find().sort('_id', -1).limit(1)[0]['_id']

        return [vouchers, ultimo_id]


    except errors.ServerSelectionTimeoutError as err:
        # Caso de error, sepasan los datos correspondientes
        cliente = None

        # Se imprime el error de conexión y se levanta un error
        print ("Error a la hora conectarse a Mongo:", err)
        return [None, None]

