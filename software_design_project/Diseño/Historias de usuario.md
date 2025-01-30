

## Se presentan las historias de usuario derivadas de la épica principal, las personas y el escenario que se identificó para el proyecto

---
#### Historia 1

 El trabajador quiere subir fotos a la página web para evitar tener que introducir los datos de manera manual, si la pagina web acepta la foto se tomara como que la historia estará realizada.

Notas: Se utilizó el framework/librería Streamlit para crear la interfaz de usuario de cero. Dentro de esta interfaz, el usuario puede hacer "drag and drop" o hacer click para buscar el archivo. El archivo se guarda en caché y se muestra en pantalla. Luego la imagen se guarda en una carpeta que por ahora hace la carpeta TempDir.

---
#### Historia 2

 El administrador desea poder descargar los datos almacenados en la base de datos para ingresarlos a la contabilidad de la empresa, si el administrador obtiene el archivo que pueda ser abierto en Excel la historia estará finalizada.

Notas: Se utilizó pymongo en conjunto con Pandas para extraer la información de la base de datos, convertirlo en un CSV y se agregó la posibilidad de filtrar las fechas entre las que se quiere extraer la data con dos inputs de fecha de Streamlit. El dataframe es finalmente convertido a CSV y se puede descargar por medio del botón de descarga.

---
#### Historia 3

 El contador quiere descargar el archivo que contiene información contable de manera completa y ordenada para realizar su trabajo, se aceptará la historia como realizada si los datos del archivo están ordenados y son correctos.

Notas: Se resolvió en la historia 2.

---
#### Historia 4

 El cliente desea visualizar la contabilidad de un periodo de tiempo desde la pagina web. Si el usuario puede visualizar la contabilidad, la historia se considera finalizada.

Notas: Se agregó la página Dashboard, que contiene diferentes gráficos que permiten un análisis fácil y rápido de la contabilidad.

---
#### Historia 5

 Contaduría  desea seleccionar la información a descargar por rango de fechas para no tener que filtrar la información en una hoja de Excel. Si el contador puede filtrar la informacion por un rango de fechas, la historia se considera finalizada.

Notas: Por medio de cajas de fecha de streamlit se permite filtrar las fechas y generar el CSV basado en las fechas que el usuario desee.

---
#### Historia 6

 El usuario desdea escanear únicamente los vouchers de las facturas para facilitar el procesamiento de los datos a la hora de ingresar la información  a contabilidad. Si en el sistema se puede ver el motivo, el total y la fecha de la transacción la historia se da por finalizada.

Notas:

---
