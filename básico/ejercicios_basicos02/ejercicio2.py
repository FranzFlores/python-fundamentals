"""
Ejercicio 2: Escribir un programa que agregue valores a una lista mientras que su longitud sea menor a 120 y luego mostrarla. 
Usar While y For.
"""

list = []
cont = 0

#Con bucle while
while cont < 120: 
    list.append(cont+1)
    cont += 1
print(list)

# Con bucle for
for i in range(120):
    list.append(i+1)

print(list)