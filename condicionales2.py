print("Verificación de acceso")

edad_usuario=int(input("Ingrese su edad: "))

if edad_usuario<18:
	print("No puede pasar")
if edad_usuario>100:
	print("Edad incorrecta") 
else:
	print("Puede pasar")
print("El programa1 ha finalizado")


edad_usuario2=int(input("Ingrese su edad: "))

if edad_usuario2<18:
	print("No puede pasar")
elif edad_usuario2>100:     # elif
	print("Edad incorrecta") 
else:
	print("Puede pasar")
print("El programa2 ha finalizado")
print("")

print("Evaluaciones")

nota_alumno=int(input("Ingrese la nota del alumno: "))

if nota_alumno<5:
	print("Insuficiente")
elif nota_alumno<6:      # elif
	print("Suficiente") 
elif nota_alumno<7:
	print("Insuficiente")
elif nota_alumno<9:
	print("Insuficiente")
else:
	print("Sobresaliente")
print("El programa Evaluaciones ha finalizado")