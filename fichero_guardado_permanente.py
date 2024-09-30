import pickle

class Persona:
	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado una persona nueva con el nombre de ", self.nombre)

	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
	personas=[]

	def __init__(self):
		
		listaDePersonas=open("ficheroExterno", "ab+") # Este ficheroExterno se almacena en nuestra carpeta donde se crea este archivo.py
		listaDePersonas.seek(0)

		try:
			self.personas=pickle.load(listaDePersonas) # Volcado y almacenamiento de datos
			print("Se cargaron {} personas del fichero externo ".format(len(self.personas)))
		except:
			print("El fichero esta vacío")
		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno() # Aquí esta una clave

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonasEnFicheroExterno(self):
		listaDePersonas=open("ficheroExterno", "wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)

	def mostrarInfoFicheroExterno(self):
		print("La formación del fichero externo es la siguiente: ")
		for p in self.personas:
			print(p)

miLista=ListaPersonas()
#p=Persona("Sandra", "Femenino", 29)
#miLista.agregarPersonas(p)

#p=Persona("Antonio", "Masculino", 39)
#miLista.agregarPersonas(p)

#p=Persona("Ana", "Femenino", 19)
#miLista.agregarPersonas(p)

persona=Persona("Antonio", "Masculino", 49) # Agrega al fichero Exrerno una nueva persona solo con una linea (sin las linas anteriores se agregaron las mismas personas)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()
#miLista.mostrarPersonas()