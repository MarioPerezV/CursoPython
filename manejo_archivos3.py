print("Modo añadir a")
from io import open # Open pide dos argumentos, más información en https://docs.python.org/3.7/library/io.html

archivo_texto=open("archivo.txt","a") #La creación y apertura se realiza con el método Open

archivo_texto.write("\n Siempre es una buena hora para estudiar Python")

archivo_texto.close()