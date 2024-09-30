print("Lista")
def generapares(limites):

	num=1

	miLista=[]

	while num<limites:

		miLista.append(num*2)

		num=num+1

	return miLista

print(generapares(10)) # genera 9 numeros pares
print("")
print("Generador")

def generaPares(limites):

	num=1

	while num<limites:

		yield num*2

		num=num+1

devuelvePares=generaPares(10)

for i in devuelvePares:
	print(i)

print("")
print("Generador II")

def generaPares(limites):

	num=1

	while num<limites:

		yield num*2

		num=num+1

devuelvePares=generaPares(10) # Estado de suspensión entre cada llamada print

print(next(devuelvePares))

print("Aquí podría ir más código...")

print(next(devuelvePares))

print("Aquí podría ir más código...")

print(next(devuelvePares))

print("Aquí podría ir más código")