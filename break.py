print("*********************************************")
print("**  while con la Sentencia break  ***********")
print("********************************************* \n")

contador = 0

while contador < 10:
    contador += 1

    if contador == 5:
        break # FINALIZA LA CONDICIÓN POR CORTE DE EJECUCIÓN

    print("Valor actual de la variable: ", contador)

print("la sentencia break se ha ejecutado")


