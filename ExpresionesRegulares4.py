# Match y search sirve para cadenas de texto extensas
# Buscar patrones de busquedas dentro de una cadena de texto extensas
import re

nombre1="Sandra Lopez"
nombre2="Loro Gomez"
nombre3="Pepe Lopez"
nombre4="Lara Lopez"
cadena1="Jara Lopez"
cadena2="35462457"
cadena3="a35462457"
codigo1="a35462457fa´c 9u4'qt8uqp943vtp7345767677"

#if re.match("sandra", nombre1, re.IGNORECASE):
#if re.match(".ara", nombre1, re.IGNORECASE):
#if re.match("\d", cadena3):
if re.search("77", codigo1):

	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")
