edad=-700

if edad<100:
	print("La edad es correcta")
else:
	print("La edad es incorrecta")

if 0<edad<100:
	print("La edad es correcta")
else:
	print("La edad es incorrecta")

print("Salarios")

salario_presidente=int(input("Ingrese el salario del presidente: "))
print("Salario presidente: " + str(salario_presidente))
# No se puede concatenar tipos diferentes en Python - print("Salarios presindete: " + salario_presidente)

salario_director=int(input("Ingrese el salario del director: "))
print("Salario director: " + str(salario_director))

salario_jefe_area=int(input("Ingrese el salario del jefe_area: "))
print("Salario jefe_area: " + str(salario_jefe_area))

salario_administrativo=int(input("Ingrese el salario del administrativo: "))
print("Salario administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")