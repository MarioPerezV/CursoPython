for i in ["Píldoras", "Informáticas", 3]:

	print("Hola", end=" ")
# Resultado: Hola Hola Hola

for i in "PíldorasInformáticas.es":

	print("Hola", end=" ")
# Resultado: Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola >>> 
print("")

email=False
miEmail=input("Ingree su email: ")

for i in miEmail:

	if(i=="@"):
		email=True# Aquí se termina la ejecución del primer if

if email:		
	print("El email es correcto")
else:
	print("El email No es correcto")
print("")

contador=0
miEmail=input("Ingree su email: ")

for i in miEmail:

	if(i=="@" or i=="."):
		contador=contador+1

if contador==2:		
	print("El email es correcto")
else:
	print("El email No es correcto")
print("")


for i in range(5):
	print("Hola")