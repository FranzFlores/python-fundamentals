"""
Modulos: Son funcionalidades ya hechas para reutlizar.
https://docs.python.org/es/3/py-modindex.html
"""
#Importat modulo propio
import mymodule

print(mymodule.helloWorld("Franz"))
print(mymodule.calculator(3,5,True))

#Importar solo una funcion del modulo
from mymodule import helloWorld
print(helloWorld("Franz"))

#Importar todo el modulo
from mymodule import *
print(helloWorld("Franz"))

#Modulos de Python
#Modulo de fechas
import datetime
print(datetime.date.today());

complete_date = datetime.datetime.now()
print(complete_date)
print(complete_date.year)
print(complete_date.month)
print(complete_date.day)

custom_date = complete_date.strftime("%d/%m/%Y")
print(custom_date)

#Modulo matematicas
import math
print("Raíz cuadrada de 9:", math.sqrt(9))
print("Número Pi:", math.pi)

print("Redondear al siguiente número próximo: ", math.ceil(6.238923))
print("Redondear al anterior número próximo: ", math.floor(6.238923))

#Modulo random
import random
print("Número aleatorio entre 15 y 20:", random.randint(15,20))