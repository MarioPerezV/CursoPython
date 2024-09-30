miLista=["María", "Pepe", "Marta", "Antonio"]

print(miLista[:])
print(miLista[0])
print(miLista[-1])
print(miLista[-2])

print(miLista[0:3])
print(miLista[2:]) # Desde 2 hasta el final

miLista.append("Sandra") # Agrega solo al final
print(miLista[:])

miLista.insert(2,"Andrés") # Agrega en cualquier posicion
print(miLista[:])

miLista.extend(["Ana", "Pía"]) # Agrega solo al final
print(miLista[:])

print(miLista.index("Ana")) # Posicion del elemento

print("Pepe" in miLista) # Se encuentra Pepe en miLista? True o False

miLista.extend([5,True, 10.4]) # no funciona agregar otros typos con .append
print(miLista[:])

miLista.remove("Ana") # 6
print(miLista[:])

miLista2=["Sandro","Pío"]*3

miLista3=miLista+miLista2
print(miLista3[:])
print("Fin del ciclo")