i=1

while i<=10:
	print("Ejecución " + str(i))
	i=i+1

print("Terminó la ejecución")
print("")

print("Bucle infinito e indeterminado")
edad=int(input("Ingrese su edad: "))

while edad<0 or edad>99:
	print("Ha ingresado una edad incorrecta, vuelva a intentarlo")
	edad=int(input("Ingrese su edad: "))

print("Gracias por su cooperación")	
print("Edad del aspirante: " + str(edad))

import math
print("Bucle finito e indeterminado")
numero=int(input("Ingrese su número: "))
intentos=0
while numero<0:
	print("No se puede hallar la raíz de un número negativo")
	
	if intentos==2: 
		print("Demasiados intentos, se cierra el programa")
		break;

	numero=int(input("Ingrese su número: "))	
	if numero<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero) # math se debe importar
	print("La raíz cuadradda de " + str(numero) + " es " + str(solucion))


