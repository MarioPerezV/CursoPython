import sqlite3

miConexion=sqlite3.connect("1PrimeraBBDD")

miCursor=miConexion.cursor() # Creacion del Cursor o Puntero

# miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))") # Creando una tabla en una BBDD

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('Balón', 15, 'Deportes')")

#variosProductos=[
	
#	("Camiseta", 10, "Deportes"),
#	("Jarrón", 90, "Cerámica"),
#	("Camión", 20, "Juguetería")
#]
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

# print(variosProductos) # Ctrl + B

for producto in variosProductos:
	print("Nombre Artículo: ", producto[0], " Sección: ", producto[2])

miConexion.commit()


miConexion.close()