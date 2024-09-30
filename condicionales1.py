print("Evaluación de notas de los alumnos")

nota_alumnos=input("Ingrese el promedio")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:              # Las 3 líneas siguietnes es el ámbito de la condicional
		valoracion="reprobado"
	return valoracion

# print(evaluacion(4))
# print(evaluacion(nota=5))
print(evaluacion(int(nota_alumnos)))
