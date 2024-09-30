# EXPRESIONES REGULARES: Son una secuencia de caracteres que forman un patrón de búsqueda para el trabajo y procesamineto de texto. Ejemplos: 1.- Buscar un texto que se ajusta a un formato determinado(correo electrónico); 2.- Buscar si existe o no una cadena de caracteres dentro de un texto; 3.- Contar el número de coincidencias dentro de un texto; entre otras (Miniprogramas para programación dentro de otro programa)

import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje sencillo"

# print(re.search("aprenderaaaa", cadena))

textoBuscar="Python"

'''if re.search(textoBuscar, cadena) is not None:
	print("He encontrado el texto")
else:
	print("No he encontrado el texto") '''

'''textoEncontrado=re.search(textoBuscar, cadena)

print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span()) '''

print(re.findall(textoBuscar, cadena))
print(len(re.findall(textoBuscar, cadena)))