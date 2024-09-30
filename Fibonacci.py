print("********************************")
print("***  Secuencia de Fibonacci   **")
print("******************************** \n")

# num_1, num_2 = 0, 1   También es válida esta línea
num_1 = 0
num_2 = 1

while num_2 <= 1597:
    print(num_1, num_2, end=" ")
    num_1 = num_1 + num_2
    num_2 = num_1 + num_2
