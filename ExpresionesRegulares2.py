# Metacaracteres
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
		'camion',
		'camión',
		'niñas',
		'Salo Reyes']

for elemento in lista_nombres:
	#if re.findall('^Sandra', elemento):
	#if re.findall('Martin$', elemento):
	#if re.findall('es$', elemento):
	#if re.findall('^ftp', elemento):
	#if re.findall('niñ[oa]s', elemento):
	if re.findall('cami[oó]n', elemento):
		print(elemento)