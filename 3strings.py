myStr = "Hello my Lord"

# Control + Shif + P = comment ###

# print(dir(myStr))

# tres formas de hacer lo mismo
print("Mi nombre es: " + myStr) #
print(f"Mi nombre es: {myStr}") 
print("Mi nombre es: {0}".format(myStr)) 

# print(myStr.upper()) # HELLO WORLD
# print(myStr.lower())
# print(myStr.swapcase())
# print(myStr.capitalize())
# print(myStr.replace('hello', 'bye').upper()) # BYE WORLD
# print(myStr.count('o')) # 2 vecesaparece la letra 'o'
# # print(myStr.startswith('hola')) # El texto comenza con 'HELLO', por lo tanto es False
# print(myStr.startswith('H')) # True
# print(myStr.endswith('d')) # True, myStr termina en 'd'
# print("")
# print(myStr.split('o')) # Sirve para separar variables a partir de cualquier elemento de la variable (se come la 'o')
# print(myStr.split('l')) # Se come la variable en la letra 'l' y la cambia por una coma

print("")
print(myStr.find('o')) # Encuentra a posicion de los caracteres de una variable
print(myStr.find('d'))

print("")
print(len(myStr)) # Longitud comienza desde el cero (-1)
print(myStr.index('e')) # El numero comienza desde el cero y "e" está en la pocisión 1

print("")
# print(myStr.isnumeric()) # False
# print(myStr.isalpha()) # True, es String

print("")
print(myStr[7]) # caracter en la posicion 7
print(myStr[0])
print(myStr[3])
print(myStr[4])
print(myStr[-1])
print(myStr[-5])