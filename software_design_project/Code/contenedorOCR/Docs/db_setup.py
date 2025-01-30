def conectar_base(str: IP_mongo, str: usuario, str: contra):

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
        print("Versión del servidor: ", cliente.server_info()["version"])

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
        res_tmp = vouchers.find({})[0]
        if not(res_tmp['_id'] == -1):
            res_tmp = vouchers.insert_one({"_id":-1,
                                           'Emisor': None,
                                           'Fecha': None,
                                           'Monto': None})
        # Obtiene el id del último elemento para seguir
        # la secuencia
        ultimo_id = vouchers.find().sort(['timestamp']).limit(1)[0]['_id']

        return [vouchers, ultimo_id]


    except errors.ServerSelectionTimeoutError as err:
        # Caso de error, sepasan los datos correspondientes
        cliente = None

        # Se imprime el error de conexión y se levanta un error
        print ("Error a la hora conectarse a Mongo:", err)
        return [None, None]
