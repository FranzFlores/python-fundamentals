"""
Funciones
def nombre_funcion(parametros):
    # código

nombre_funcion(parametros)
"""

#Ejemplo 1
# Definir función
# from __future__ import division


# def printName():
#     print("Franz")
#     print("Emilio")
#     print("Juan")
# #Invocar función
# printName()

# #Ejemplo 2 (Funciones con parámetros)
# def printYourName(name,age):
#     print(f"Tu nombre es {name}")
#     if(age>=18):
#         print("Eres mayor de edad")
#     else: 
#         print("Eres menor de edad")

# name = input("Ingresa tu nombre: ")
# age = int(input("Ingresa tu edad: "))
# printYourName(name,age)

# #Ejemplo 3 
# def table(number):
#     print(f"La tabla de multiplicar del número {number}")
#     for i in range(1,11):
#         operation = number * i
#         print(f"{number} x {i} = {operation}")
# table(3)

# #Ejemplo 4 (Parámetros opcionales)
# def getEmployee(name, dni = None):
#     print(f"Nombre: {name}")
#     if dni:
#         print(f"DNI: {dni}")
# getEmployee("Franz")

#Ejemplo 5 (Parámetros opcionales y devolver datos)
def calculator(num1,num2, op = False):
    add = num1 + num2
    subtraction = num1 - num2
    string_print = ""
    string_print += f"Suma: {num1} + {num2} = {add}\n" 
    string_print += f"Resta: {num1} - {num2} = {subtraction}\n" 

    if op:
        multiplication = num1 * num2
        division = num1 / num2
        string_print += f"Multiplicación: {num1} * {num2} = {multiplication}\n"
        string_print += f"División: {num1} / {num2} = {division}\n"

    return string_print

print(calculator(2,3,True))

#Ejemplo 6 Funciones anidadas
def get_name(name):
    text = f"Hola {name}"
    return text

def get_age(age):
    text = f"Tienes {age} años"
    return text

def get_text(name,age):
    text = f"{get_name(name)}\n{get_age(age)}"
    return text

print(get_text("Franz",18))

#Ejemplo 7 (Funciones lambda) Es una función anónima
getYear = lambda year: f"El año es {year}"
print(getYear(2014))

#Variable global: anteponer global 
global name

#Funciones Predefinidas
name = "Franz Flores"

print(name)

print(f"El tipo de variable es: {type(name)}")

# Si una variable es instancia de una clase
comprobe = isinstance(name,str)
if comprobe:
    print("Es una cadena")
else: 
    print("No es una cadena")

# Limpiar los espacios a los lados
text = "    Mi Texto      "
print(text.strip())

#Eliminar Variables 
year = 2022
print(year)
del year

#Comprobar variable vacia
text = "  ff  "
if len(text) <=0:
    print("La variable está vacía")
else:
    print("La variable tiene contenido", len(text))

#Encontrar caracteres
frase = "Hola mundo"
print(frase.find("mundo"))

#Reemplazar caracteres
new_text = frase.replace("Hola","Adios")

# Mayusculas 
print(name)
print(name.lower())
print(name.upper())

# Es recomendable declarar las funciones en la parte superior del código
# Es mejor usar return en las funciones en lugar del print
# Pasar parametros por valor o referencia