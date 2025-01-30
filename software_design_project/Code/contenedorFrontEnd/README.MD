## Front End

El front end esta compuesto por un archivo Home.py, dos páginas adicionales que se encuentran en la carpeta pages

El front end está construído principalmente usando la librería Streamlit, la cual facilita la creación de aplicaciones web. Entre las funciones utilizadas se tiene
- streamlit.write: Muestra texto formateado
- streamlit.header: Muetra texto formateado como header
- streamlit.file_uploader: Permite subir archivos a la misma interfaz
- streamlit.image: Permite mostrar imágenes en la página

entre otras.

La estructura de archivos y la explicación de cada uno se puede ver aquí abajo:

- FrontEnd
    - Home.py
    Contiene el código para el índice de la página.
    - pages
        - 1 - Subida.py
        Contiene el código para la página en la que se suben los archivos. En esta página se tiene un widget que permite que se suban archivos como drag and drop o explorando archivos locales. Al subir un archivo este lo guarda en el volumen compartido con el contenedor de OCR
        - 2 - Dashboard.py
        En este archivo está el código para el dasboard de la aplicación. Contiene código para hacer querying a la base de datos y devolver toda la data que se encuentra en la base de datos. Dentro de este archivo se convierte el JSON retornado por MongoDB a un dataframe en Pandas, el cual se manipula para conseguir las diferentes agregaciones para generar los diferentes gráficos que se encuentran en la página.
        Además de esto, contiene el código necesario para generar el archivo CSV a descargar.
    - dependencies
        - DB.py
        Contiene el código necesario para fetch información de la base de datos. Usa la librería pymongo para conectarse a la instancia de MongoDB y así poder retornar la data como un JSON.