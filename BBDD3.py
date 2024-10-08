import sqlite3

miConexion=sqlite3.connect("2GestionProductos")

miCursor=miConexion.cursor()


miCursor.execute('''
	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50),
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

productos=[
	("pelota", 20, "juguetería"),
	("pantalón", 15, "confección"),
	("destornillador", 25, "ferretería"),
	("jarrón", 45, "cerámica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos) # Este código sirve para agregar elementos a la BBDD

miConexion.commit()


miConexion.close()