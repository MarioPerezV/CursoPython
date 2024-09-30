# CONDICIONALES

color = "green"
x = 7
# 3 = 3 asignando
# 3 == 3 comparando

if x < 30:
    print("x is less than 30")
if x == 30:
    print("x is equals than 30")
else:
    print("x is more than 30")

# Otra forma de hacer lo mismo
if color == "red":
    print(color)
elif color == "blue":
    print(color)
else:
    print("Any color")

name = "Jhon"
lastname = "Carter"

# Ojo con INDENTADO, sin eso no imprime
if name == "Jhon":
    if lastname == "Carter":
        print("You are Jhon Carter")
    else:
        print("You are not Jhon Carter")

if x > 2 and x <= 10: # Tenía un espacio al inicio y me marcó un error
     print("x es mayor que 2 y menor o igual que 10")
     
if x > 2 or x <= 20:
     print("x es mayor que 2 o menor igual que 20")
     
if (not(x == y)):
     print("x no es igual que y")
