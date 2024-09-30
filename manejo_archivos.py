print("Modo escritura .write()")
from io import open # Open pide dos argumentos, más información en https://docs.python.org/3.7/library/io.html

archivo_texto=open("archivo.txt","w") #La creación y apertura se realiza con el método Open

frase="Estupendo día para estudiar Python \n es viernes, yahooooo!!!!" # Manipulación instrucción

archivo_texto.write(frase) # Manipulación ejecuta

archivo_texto.close()
