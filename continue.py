print("*********************************************")
print("**  while con la Sentencia continue  ********")
print("********************************************* \n")

contador = 0

while contador < 10:
    contador += 1

    if contador == 5:
        continue # SE SALTÓ EL print VOLVIENDO AL while

    print("Valor actual de la variable: ", contador)

print("la sentencia continue se ha ejecutado")
