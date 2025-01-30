**Objetivo:**
	- Desarrollar un prototipo de sistema de registro contable que mediante un OCR obtenga los datos de una fotografía, y se salve todo en una base de datos.

El patrón de diseño es un MVC, que se especifica en el siguiente diagrama:

```plantuml
@startuml

component Modelo {

	port a

	component "Contenedor OCR" as OCR
	component "Contenedor Base de datos" as db
	OCR --> db

}

component Controlador {

	port b

}

component Vista {

	port c

}


note left of Modelo : -Valida las imágenes\ningresadas\n-Prepara archivos\nde salida

note bottom of Controlador : -Obtiene interfaz\n-Dirige imágenes\nal Modelo\n-Dirige datos disponibles\na Vista

note bottom of Vista : -Permite cargar imágenes\n-Lista datos disponibles\n-Consiste en una\ninterfaz web

a <-> b
b <-> c


@enduml
```

Es necesario aclarar que la interconexión entre las capas se lleva a cabo mediante un volumen de docker, esto porque la naturaleza del producto desarrollado (dígase un prototipo) requiere mostrar resultados en el tiempo definido, de disponer de un rango de tiempo mayor se podría implementar una base de datos SQL que permita su acceso por https, de modo que no sea necesaria la conexión entre volúmenes.