print("Calculadora con 2 variables. \n")

print("********************************")
print("***Menu de opciones*************")
print("******************************** \n")

print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicación")
print("4.- División")
print("5.- División entera")
print("6.- Exponente")
print("7.- Módulo o resto \n")

numero = int(input("Introduzca la opcion deseada: "))

if numero == 1:
    print("Elegiste Suma \n")
    numero = int(input("Ingrese el primer número: "))
    numero += int(input("Ingrese el segundo número: "))
    print("El resultado de la Suma es: ", numero)

elif numero == 2:
    print("Elegiste Resta \n")
    numero = int(input("Ingrese el primer número: "))
    numero -= int(input("Ingrese el segundo número: "))
    print("El resultado de la Resta es: ", numero)

elif numero == 3:
    print("Elegiste MUltiplicación \n")
    numero = int(input("Ingrese el primer número: "))
    numero *= int(input("Ingrese el segundo número: "))
    print("El resultado de la Multiplicación es: ", numero)

elif numero == 4:
    print("Elegiste División \n")
    numero = float(input("Ingrese el primer número: "))
    numero /= float(input("Ingrese el segundo número: "))
    print("El resultado de la División es: ", round(numero, 2))

elif numero == 5:
    print("Elegiste División Entera \n")
    numero = int(input("Ingrese el primer número: "))
    numero //= int(input("Ingrese el segundo número: "))
    print("El resultado de la División Entera es: ", numero)
    
elif numero == 6:
    print("Elegiste Exponentes \n")
    numero = int(input("Ingrese el primer número: "))
    numero **= int(input("Ingrese el segundo número: "))
    print("El resultado de la Exponentes es: ", numero)

elif numero == 7:
    print("Elegiste Módulo o Resto \n")
    numero = int(input("Ingrese el primer número: "))
    numero %= int(input("Ingrese el segundo número: "))
    print("El resultado de la Módulo o Resto es: ", numero)

else:
    print("La opción ingresada incorrecta")










    
