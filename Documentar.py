# Documentar un programa para ayudamemoria

class Areas:
			
	def areaCuadrado(lado):
		""" También sirve triple comillas
		para varias
		lineas"""
		return "El área del cuaderado es: " + str(lado*lado)

	def areaTriangulo(base, altura):
		""" Además se puede imprimir en pantalla
		esta documentación con la funcion print y help"""
		return "El área del triangulo es: " + str(base*altura)

#print(areaTriangulo(2,7))
#print(areaCuadrado(5))
#print(areaCuadrado.__doc__)

help(Areas)