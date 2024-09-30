from io import open # Open pide dos argumentos, más información en https://docs.python.org/3.7/library/io.html

archivo_texto=open("archivo.txt","r")

# print(archivo_texto.read(11)) # imprime hasta la posición 11 y la nueva lectura (print) comienza desde este punto
# archivo_texto.seek(10) # Seek (Puntero a partir de donde se repita la información)
# print(archivo_texto.read()) # No imprime dos veces el mismo archivo a menos que se agregue un puntero Seek

# archivo_texto.seek(len(archivo_texto.read())/2) # len cantidad de caracteres (/2 = a la mitad)
print(archivo_texto.read())

