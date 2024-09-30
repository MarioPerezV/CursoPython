print("Generador I")
def devuelveCiudades(*cuidades):
	for elemento in cuidades:
		yield elemento

cuidades_devueltas=devuelveCiudades("Madrid", "Barcelona", "Bilbao")

print(next(cuidades_devueltas))

print(next(cuidades_devueltas))
print("")

print("Generador II")
def devuelveCiudades(*cuidades):
	for elemento in cuidades:
		for subElemento in elemento:
			yield subElemento

cuidades_devueltas=devuelveCiudades("Madrid", "Barcelona", "Bilbao")

print(next(cuidades_devueltas))

print(next(cuidades_devueltas))
print("")

print("Generador III")
def devuelveCiudades(*cuidades):
	for elemento in cuidades:
		# for subElemento in elemento:
			yield from elemento

cuidades_devueltas=devuelveCiudades("Madrid", "Barcelona", "Bilbao")

print(next(cuidades_devueltas))

print(next(cuidades_devueltas))
