''' DECORADORES: Son funciones que a su vez añaden funcionalidades a otras funciones. Por esto se les denomina "Decoradores", porque "decoran" a otras funciones. Les añaden funcionalidades.
Estructura de un Decorador:
A) tiene 3 funciones (A, B y C) donde A recibe como parámetro a B para devolver C
B) un decorador devuelve una funcion
	def funcion_decorador "A"(función "B"):
		def funcion_interna "C"():
			# código de la funcion interna
		return funcion_interna
	@funcion_decorador "A"
'''
def funcion_decoradora(funcion_parametro):
	def funcion_interior():
		# Acciones adicionales que decoran
		print("Vamos a realizar un cálculo: ") # Se puede abrir una base de datos
		
		funcion_parametro() # Cuando se ejecuta o establece una función o conexión

		print("Hemos terminado el cálculo") # Se cierra la conexion de BBDD
	return funcion_interior

@funcion_decoradora # También se puede agregar antes de cada función
def suma():
	print(15+20)

@funcion_decoradora
def resta():
	print(30-10)

suma()
resta()