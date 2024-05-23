print("############ Ejercico 1 ############")
# Condicionales básicos
color = input("Ingrese un color: ")

if color == 'rojo':
    print("El color es rojo")
else:
    print("El color no es rojo")

# Condicionales con operadores de comparacion
print("############ Ejercico 2 ############")
year = int(input("Ingrese un año: "))
if year >= 2021:
    print("El año es mayor o igual a 2021")
else:
    print("El año es menor a 2021")

# Condicionales con ifs anidados
print("############ Ejercico 3 ############")
nombre = "Franz Flores"
ciudad = "Loja"
continente = "América"
edad = 23
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if ciudad == "Loja":
        print(f"{nombre} vive en {ciudad}")
    else:
        print(f"{nombre} no vive en {ciudad}")
else:
    print(f"{nombre } es menor de edad")

# Condicionales con elif
print("############ Ejercico 4 ############")
dia = int(input("Ingrese un dia: "))
if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es fin de semana")

# Operadores logicos con multiples condiciones
print("############ Ejercico 5 ############")
edad_minima = 18
edad_maxima = 65
edad_oficial = 17

""" 
Operadores logicos:
and Y
or O
! negacion
not no
"""

if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print("Esta en edad para trabajar")
else:
    print("No esta en edad para trabajar")

