import math

def raizCuadrada(listaNumeros):
	"""
	La función devuelve una lista con la 
	raiz cuaddrada de los elementos numéricos 
	pasados poe parámetros en otra lista

	>>> lista=[]
	>>> for i in [4,9,16]:
	...		lista.append(i)
	>>> raizCuadrada(lista)
	[2.0, 3.0, 4.0]


	"""

	return [math.sqrt(n) for n in listaNumeros]

print(raizCuadrada([9,16,25,36]))

"""import doctest
doctest.testmod()"""