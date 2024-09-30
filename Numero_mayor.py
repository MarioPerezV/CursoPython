print("Cuál es el numero mayor?")

num_1 = int(input("Ingrese el 1er número: "))
num_2 = int(input("Ingrese el 2do número: "))
num_3 = int(input("Ingrese el 3er número: "))

if num_1 > num_2 and num_1 > num_3:
    print(num_1, " es el mayor de los números ingresados")
else:
    if num_2 > num_3:
        print(num_2, " es el mayor de los números ingresados")
    else:
        print(num_3, " es el mayor de los números ingresados")
