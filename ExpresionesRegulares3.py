# Rangos
import re
lista_nombres=[
		'ftp://pildorasinformaticas.es',
		'http://ecoma.cl',
		'ftp://pildorasinformaticas.com',
		'Ana Gomez',
		'Maria Martin',
		'Sandra Lopez',
		'Sandra Feña',
		'niños',
		'Celia',
		'Rosa',
		'camion',
		'Pedro',
		'camión',
		'Ma1',
		'Ma3',
		'Ma2',
		'Ma4',
		'MaB',
		'MaX',
		'MaC',
		'Ma.Z',
		'niñas',
		'Salo Reyes']

for elemento in lista_nombres:
	
	#if re.findall('[o-t]$', elemento):
	#if re.findall('[O-T]', elemento):
	#if re.findall('Ma[0-3]', elemento):
	#if re.findall('Ma[0-3A-B]', elemento):
	if re.findall('Ma[.:]', elemento):
		print(elemento)