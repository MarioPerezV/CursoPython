import sqlite3

miConexion=sqlite3.connect("1GestionProductos")

miCursor=miConexion.cursor()


miCursor.execute('''
	CREATE TABLE PRODUCTOS(
	CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
	NOMBRE_ARTICULO VARCHAR(50),
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

productos=[
	("ARO1", "pelota", 20, "juguetería"),
	("ARO2", "pantalón", 15, "confección"),
	("ARO3", "destornillador", 25, "ferretería"),
	("ARO4", "jarrón", 45, "cerámica")

]

# miCursor.execute("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'tren', 15, 'juguetería')") # Este código sirve para agregar elementos a la BBDD

miConexion.commit()


miConexion.close()