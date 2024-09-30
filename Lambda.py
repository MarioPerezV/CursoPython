# calcular repetidamente un área de un triángulo con Lambda
def area_triangulo(base,altura):
	return(base*altura)/2

# print(area_triangulo(5,7))  # OPCION 1

'''triangulo1=area_triangulo(5,7)   # OPCION 2
triangulo2=area_triangulo(9,6)
print(triangulo1)
print(triangulo2)'''

area_triangulo=lambda base,altura:(base*altura)/2   # OPCION 3
'''print(area_triangulo(7,5))  # OPCION 3.1
print(area_triangulo(9,6))'''

triangulo1=area_triangulo(5,7)   # OPCION 3.2
triangulo2=area_triangulo(9,6)
print(triangulo1)
print(triangulo2)