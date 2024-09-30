class Empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):
		return"{} que trabaja como {} tiene un salario de $ {}".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
Empleado("Juan", "Director", 75000),
Empleado("Ana", "Presidenta", 85000),
Empleado("Juana", "Administrativo", 25000),
Empleado("Joan", "Secretaria", 27000),
Empleado("Mario", "Botones", 21000)
]

salarios_altos=filter(lambda empleado:empleado.salario>50000, listaEmpleados)

for emplado_salario in salarios_altos:
	print(emplado_salario)