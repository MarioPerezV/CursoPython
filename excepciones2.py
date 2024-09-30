def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1, num2):		
	try:
		return num1/num2 # Para evitar una excepción o error

	except ZeroDivisionError:
		print("No se puede dividir sobre cero")
		return "Operación errónea"

while True: # Sirve para que se repita la solicitud de datos hasta que ingrese valores válidos
	try:	
		op1=(int(input("Ingrese el primer número: ")))

		op2=(int(input("Ingrese el segundo número: ")))			
		break

	except ValueError:
		print("Los valores introducidos no son correctos, intentelo nuevamente")
		
operacion=input("Inrese la operación a realizar (suma,resta,multiplica,divide): ")
operacion.lower()

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")
print("")

def divide():

	try:
		op1=(float(input("Ingrese el primer valor: ")))
		op2=(float(input("Ingrese el segundo valor: ")))
		print("La división es: " + str(op1/op2))
	except ValueError:	
		print("El valor introducido no es correcto") # Puede ser " Ha ocurrido un error" no es preciso
	except ZeroDivisionError:
		print("No se puede dividir sobre cero")
	finally:# Aquí esto es irrelevante pero si ocurre un error este finally se ejecuta
		print("Calculo finalizado")
divide()