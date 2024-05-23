"""
Ejercicio 3. Escribir un programa que muestre los cuadrados de los primeros 60 números naturales.
Resolverlo con un bucle for y con un bucle while.
"""

# While
cont = 1
while cont <= 60:
    print(f"El cuadrado de {cont} es {cont**2}")
    cont += 1

print("\n")

# For
for number in range(1,61):
    print(f"El cuadrado de {number} es {number**2}")