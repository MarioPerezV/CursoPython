import sqlite3

miConexion=sqlite3.connect("3GestionProductos")

miCursor=miConexion.cursor()

# UNIQUE se utiliza para que No se repita el nombre_articulo. ---- TAMPOCO SE PUEDEN INCLUIR COMENTAIOS DENTRO DE LAS LÍNEAS DEL CODIGO SQLite
# miCursor.execute('''
# 	CREATE TABLE PRODUCTOS (
# 	ID INTEGER PRIMARY KEY AUTOINCREMENT,
# 	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
# 	PRECIO INTEGER,
# 	SECCION VARCHAR(20))
# ''')

# productos=[
# 	("pelota", 20, "juguetería"),
# 	("pantalón", 15, "confección"),
# 	("destornillador", 25, "ferretería"),
# 	("jarrón", 45, "cerámica"),
# 	("pantalones", 35, "confección")
# ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos) # Este código sirve para agregar elementos a la BBDD

#------BUSQUEDA DE ELEMENTOS DE confección----
# miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección'")

#------ACTUALIZACIÓN/MODIFICACIÓN DE ELEMENTOS----
# miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

#------ELIMINACIÓN DE ELEMENTOS ---------
# miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")


productos=miCursor.fetchall()

print(productos)

miConexion.commit()


miConexion.close()