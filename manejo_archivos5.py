from io import open 

archivo_texto=open("archivo.txt","r+") # r+ = Lectura y escritura

# archivo_texto.write("Comienzo del texto") # Reemplaza la primera linea de texto

# print(archivo_texto.readlines())

lista_texto=archivo_texto.readlines();

lista_texto[1]=" Esta línea ha sido reemplazada desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()