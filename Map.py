# FUNCION MAP: Aplica una función a cada elemento de una lista iterable (listas, tuplas, etc) devolviendo una lista con los resultados.
class Empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):
		return"{} que trabaja como {} tiene un salario de $ {}".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
Empleado("Juan", "Director", 7500),
Empleado("Ana", "Presidenta", 8500),
Empleado("Juana", "Administrativo", 2500),
Empleado("Joan", "Secretaria", 2700),
Empleado("Mario", "Botones", 2100)
]

def calculo_comision(empleado):
	if empleado.salario>=2500:
		empleado.salario=empleado.salario*1.03
	return empleado

listaEmpleadosComision=map(calculo_comision, listaEmpleados)

for empleado in listaEmpleadosComision:
	print(empleado)