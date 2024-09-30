producto = { # Diccionario
    "name": "book",
    "quantity": 3,
    "price": 10.99
}

productos = [ # Separados por llaves
    {"name": "book", "price": 10.00},
    {"name": "laptop", "price": 1000}
]

print(producto)

persona = { # no van separados dentro del diccionario
    "first_name": "Ryan",
    "last_name": "Ray"
}

print(type(producto))
print(persona.keys()) # first_name, last_name
print(persona.items()) # first_name: Ryan, last_name: Ray
print("")
print(persona)
print("")
print(producto)

carro = [ # Por un espacio al inicio marca un error
     {"book": 3, 4: 99},
     {"rock": 3, 4: 89},
     {"ice": 3, 4: 79},
     {"sour": 3, 4: 69},
 ]
print(carro)