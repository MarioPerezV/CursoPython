def evaluaEdad(edad):
	if edad<0:
		raise TypeError("No se permiten edades negativas")

	if edad<20:
		return "Eres muy joven"
	elif edad<40:
		return "Eres joven"
	elif edad<65:
		return "Eres maduro"
	elif edad<100:
		return "Cuidese..."
	
print(evaluaEdad(43))
print("")

import math

def calculaRaiz(num1):
	if num1<0:
		raise ValueError("El número no puede ser negativo")
	else:
		return math.sqrt(num1)

op1=(int(input("Ingrese un valor: ")))

try:
	print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)
	print("Programa finalzado")
print("")

def evaluaEdad(edad):
	if edad<0:
		raise MipropioError("No se permiten edades negativas")

	if edad<20:
		return "Eres muy joven"
	elif edad<40:
		return "Eres joven"
	elif edad<65:
		return "Eres maduro"
	elif edad<100:
		return "Cuidese..."
	
print(evaluaEdad(-15))	