#CONDICIONALES SIMPLES, COMPUESTAS, MÚLTIPLES y ANIDADAS:
"""
print("Sistema para calcular  el promedio del alumno en el año.")
            
nombre = input("Nombre del alumno: ")

matematicas = float(input(nombre + ". Ingresa calificación de matematicas: ")) # "float" se usa para decimales
quimica = float(input(nombre + ". Ingresa calificación de quimica: "))
biologia = float(input(nombre + ". Ingresa calificación de biología: "))

promedio = (matematicas + quimica + biologia) / 3
#promedio = int(promedio)   NO SE USA EN CONDICIONAL COMPUESTO, SOLO EN EL SIMPLE

if promedio >= 4:
    print('Felicidades ' + nombre + ', ha sido "Aprobado" con promedio:', promedio) # Simbolo + sirve para str, mas no int
    print('Felicidades ' + nombre + ', ha sido "Aprobado" con promedio:', round(promedio,2))

#print("Fin.") # Condicional simple
else:   # Condicional compuesto
    print(nombre + ' . Lamentablemente has "Reprobado" con promedio:', promedio) 
    print(nombre + ' . Lamentablemente has "Reprobado" con promedio:', round(promedio,3))

print("FIN")
"""

# CONDICIONALES MULTIPLES
"""
print("====================================")
print("Convertidor de números a letras.")
print("====================================")

num_uno = int(input("¿Cuál es el número que desea convertir?: "))

if num_uno == 1:
    print("El número es Uno")
elif num_uno == 2:
    print("El número es Dos")
elif num_uno == 3:
    print("El número es Tres")
elif num_uno == 4:
    print("El número es Cuatro")
elif num_uno == 5:
    print("El número es Cinco")
else:
    print("Ninguna de las condiciones se ha cumplido, este programa puede convertir hasta el número 5")

print("FIN")
"""
# CONDICIONAL ANIDADA

print("====================================")
print("Conversor.")
print("==================================== \n")

print("Menú de opciones: \n")
print("Presione 1 para convertir de número a palabra.")
print("Presione 2 para convertir de palabra a número \n")

opcion = int(input("¿Cuál es tu opcion deseada?: "))

if opcion == 1:
    print("\n Conversor de número a palabra. \n")
    
    opcion_uno = int(input("¿Cuál es el número que deseas convertir a palabra?: "))

    if opcion_uno == 1:
        print("El número es Uno")
    elif opcion_uno == 2:
        print("El número es Dos")
    elif opcion_uno == 3:
        print("El número es Tres")
    elif opcion_uno == 4:
        print("El número es Cuatro")
    elif opcion_uno == 5:
        print("El número es Cinco")
    else:
        print("El número no esta registrado")
        
elif opcion == 2:
    print("\n Conversor de palabra a número. \n")

    opcion_dos = input("¿Cuál es la palabra que deseas convertir a número?: ")
    opcion_dos = opcion_dos.lower() # .lower() METODO PARA PASAR TEXTO INGRESADO DE MAYUSCULAS A minusculas

    if opcion_dos == "uno":
        print("El número es 1")
    elif opcion_dos == "dos":
        print("El número es 2")
    elif opcion_dos == "tres":
        print("El número es 3")
    elif opcion_dos == "cuatro":
        print("El número es 4")
    elif opcion_dos == "cinco":
        print("El número es 5")
    else:
        print("El número no esta registrado")
    
else:
    print("Opción no disponible.")

print("FIN")


















