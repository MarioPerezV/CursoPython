print("Programa de becas 2019, Operadores and y or")
print("")
distancia_escuela=int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos=int(input("Introduzca el n° de hermanos en el centro: "))
print(numero_hermanos)

salario_familiar=int(input("Ingrese el salario anual bruto "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:

	print("Tiene derecho a beca")

else:
	print("No tiene derecho a beca")
print("")

print("Programa de becas 2019, Operador in")

print("Asignaturas optativas 2019")
print("Informática gráfica - Pruebas de software")
opcion=input("Escriba la asignatura elegida: ")

asignatura=opcion.capitalize() # Para evitar que genere un error al escribir en minúsculas o alternadamente con mayusculas

if asignatura in ("Informática gráfica", "Pruebas de software"):
	print("Asignatura escogida: " + asignatura)
else:
	print("La asignatura escogida no está contemplada")


