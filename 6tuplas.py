x = (1,2,3)
z = (1,) # tupla de un solo elemento debe llevar coma ","
print (x)
print (type(x))

y = tuple((1, 2, 3))
print(y)

# print(dir(x))

print(type(x))

locations = {
    (35.123, 39.000):"Tokyo",
    (25.123, 139.000):"New York",
}
print(locations)

del x
print(x)