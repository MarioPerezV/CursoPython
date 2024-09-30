# Listas
demo_lista = [1, 'hello', 1.34, True, [1, 2, 3]]
colors = ['red', 'green', 'blue', '']

numeros_lista = list((1, 2, 3, 4)) # Se transforma en una tupla cuando varias variables se traspasan a una, ya queda inmutable hasta bueva ibstrucción
print(numeros_lista)
print(type(numeros_lista))

rango = list(range(1, 101)) # (inicio, fin)
print(rango)

# print(dir(colors))
print(type(colors))
print(len(colors)) # Cantidad de elementos en una lista
print(len(demo_lista))
print(colors[2])
print(colors[1])
print(colors[0]) # Las posiciones comienzan en '0'
print(colors[-1])
print(colors[-2])
print(colors[-3]) # Los numeros negativos son el orden inverso de las posiciones
print('green' in colors) # True
print('violet' in colors) # False

print(colors)
colors[1] = 'yellow' # Se modifica la lista
print(colors)

colors.append('violet') # sirve para agregar elementos inconmutables en una lista
print(colors)
colors.extend(['Yellow', 'Black'])
print(colors)
colors.sort() # Ordena alfabeticamente

colors.sort(reverse=True) # Ordena sentido contrario al alfabeticamente
colors.insert(-1, 'black')
colors.insert(len(colors), 'violet') # Se ingresa al final
print(colors)

colors.remove('Black')
print(colors)

print(colors.index('blue')) # Está cuarto, pero empieza desde cero
print("")
print(colors.count('red')) # Está cuarto, pero empieza desde cero
print("")

colors.pop(1) # Remueve el ultimo valor de la lista
print(colors)
colors.pop(2) # Remueve el ultimo valor de la lista
print(colors)
print("")

colors.clear()
print(colors)


