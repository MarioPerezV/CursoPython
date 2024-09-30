class Vehiculos():

	def __init__(self, marca, modelo):

		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
			self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


class Furgon(Vehiculos): # El constructor lo hereda de Vehículos
	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "El furgón está cargado"
		else:
			return "El furgón No está cargado"


class Moto(Vehiculos):# Moto Heredando de la clase Vehículos
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy haciendo caballito"
	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
			self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)


class VElectricos(Vehiculos):
	def __init__(self, marca, modelo):
		super().__init__(marca,modelo)
		self.autonomia=100

	def cargarenergia(self):
		self.cargando=True

miMoto=Moto("Yamaha", "YBR") # Llamando al Constructor
miMoto.caballito() # Este método permite la ejecución del método estado()
miMoto.estado() # La sobreescritura de codigo Estado depende del método caballito()

miFurgon=Furgon("Renault", "Kangoo") # Llamando al Constructor
miFurgon.arrancar()
miFurgon.estado()
print(miFurgon.carga(True))


class BiciElectrica(VElectricos,Vehiculos): # Herencia múltiple (dos clases, primero superclase y luego subclase)
	pass

miBiciElectrica=BiciElectrica("Oxford", "CTM")