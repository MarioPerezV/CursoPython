for i in range(5):
	print(f"Valor de la variable {i}")
print("")

for i in range(5,50,3): # 3 parámetros: desde,hasta,intervalo
	print(f"Valor de la variable {i}")
print("")

valido=False
email=input("Ingrese su email: ")
for i in range(len(email)):
	if email[i]=="@":
		valido=True
if valido:		
	print("Email Correcto")
else:
	print("Email Incorrecto")
print("")
