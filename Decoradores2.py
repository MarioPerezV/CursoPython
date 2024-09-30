# *args
def funcion_decoradora(funcion_parametro):
	def funcion_interior(*args, **kwargs): # * numero indeterminado de parámetros con el nombre args u otro
		# Acciones adicionales que decoran
		print("Vamos a realizar un cálculo: ") # Se puede abrir una base de datos
		
		funcion_parametro(*args, **kwargs) # Cuando se ejecuta o establece una función o conexión

		print("Hemos terminado el cálculo") # Se cierra la conexion de BBDD
	return funcion_interior

@funcion_decoradora # También se puede agregar antes de cada función
def suma(num1, num2):
	print(num1+num2)

@funcion_decoradora
def resta(num1, num2):
	print(num1-num2)

@funcion_decoradora
def potencia(base, exponente):
	print(pow(base, exponente))

suma(7,5)
resta(12,10)
#potencia(5,3) # Sin **kwargs
potencia(base=5,exponente=3)