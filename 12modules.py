# own modules
# thirdy party modules
# python modules
import datetime
print(datetime.date.today())
print(datetime.timedelta(minutes=100))

# Para resumir
from datetime import timedelta, date
print(date.today())

import fmath

fmath.add(1,2)
fmath.substract(1,2)

from fmath import add, substract
add(1,2)
substract(1,2)

from colorama import Fore, Style, init
init(convert=True)
print (Fore.RED + "Hello world")

