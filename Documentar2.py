""" Ejemplo 1:
def areaTriangulo(base,altura):
	Aquí deben ir 3 comillas dobles de apertura
	Calcula el área de un triangulo y la prueba .testmod siguiente se comprueba sin ejecutarlo

#	>>> areaTriangulo(3,6)
	'El área del triangulo es: 9.0'

#	>>> areaTriangulo(4,5)
	'El área del triangulo es: 10.0'

#	>>> areaTriangulo(9,3)
	'El área del triangulo es: 13.5'
	
	Aquí deben ir 3 comillas dobles de cierre
	return "El área del triangulo es: " + str((base*altura)/2)
"""
"""import doctest
doctest.testmod()"""
#------------------------------------------------
# Ejemplo 2
def compruebaMail(mailUsuario):
	"""
La funcion compruebaMail evalúa un mail
recibido en busca de la @. Si tiene una @
es correcto, si tiene más de una @ es incorrecto
si la @ está al final es incorrecto

	>>> compruebaMail('juan@cursos.es')
	True
	>>> compruebaMail('juan@cursos.es@')
	False
	>>> compruebaMail('juancursos.es')
	False
	>>> compruebaMail('juan@cursos@.es')
	False

	"""
	arroba=mailUsuario.count('@')

	if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
		return False
	else:
		return True

import doctest
doctest.testmod()