print("Modo lectura .read()")
from io import open # Open pide dos argumentos, más información en https://docs.python.org/3.7/library/io.html

archivo_texto=open("archivo.txt","r") #La creación y apertura se realiza con el método Open

lineas_texto=archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto)
print(lineas_texto[1])
