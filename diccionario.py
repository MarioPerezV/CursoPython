miDiccionario={"Alemania":"Berlin",23:"Jordan","Francia":"París","Inglaterra":"Londres","España":"Madrid","Mosqueteros":3}
print(miDiccionario["Francia"])
print(miDiccionario)

miDiccionario["Italia"]="Lisboa"
miDiccionario["Italia"]="Roma"
print(miDiccionario)

del miDiccionario["Inglaterra"]
print(miDiccionario)

miTupla=["Francia","Inglaterra","España","Alemania"]

miDiccionario={miTupla[0]:"París", miTupla[1]:"Londres", miTupla[2]:"Madrid", miTupla[3]:"Berlín"}
print(miDiccionario["Francia"])

miDiccionario2={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario2["Equipo"])
print(miDiccionario2["anillos"])
print(miDiccionario2.keys())
print(miDiccionario2.values())
print(len(miDiccionario2))
