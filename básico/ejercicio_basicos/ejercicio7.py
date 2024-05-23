"""
Ejercicio 7. Hacer un programa que muestre todos los números impares entre dos números que el 
usuario decida.
"""

num1 = int(input("Ingrese el extremo izquierdo del intervalo: "))
num2 = int(input("Ingrese el extremo derecho del intervalo: "))
intervalo = ""

if num1 < num2:
    for cont in range(num1,(num2+1)):
        if cont % 2 == 1:
            intervalo += str(cont) + ", "
else:
    print("El intervalo debe ser de menor a mayor")

print(f"[ {intervalo} ]")


