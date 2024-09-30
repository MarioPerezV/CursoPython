# FUNCIONES

# print("")
# dir(x)
# print(type(10.4))


def hello():
    print("hello world")

hello() # Esta línea ejecuta la instrucción anterior "def"

def hello(name):
    print("hello " + name)

hello("Joe")
hello("ryan")
hello("fazt")


def add(num1, num2):
    return num1 + num2

print(add(10, 30))
print(add(600, 10))

print(len("Hello"))

add = lambda num1, num2: num1 + num2 # Una programación de una suma en una sola línea
print(add(20, 45))