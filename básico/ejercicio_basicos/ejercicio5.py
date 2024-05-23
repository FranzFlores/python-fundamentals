"""
Ejercicio 5. Hacer un programa que muestre todos los numeros en un rango que ingrese el usuario.
"""

num1 = int(input("Introduce el número límite por la izquierda: "))
num2 = int(input("Introduce el número límite por la derecha: "))

print_numbers = str(num1)

for cont in range((num1+1), (num2+1)):
    print_numbers = print_numbers + ", " + str(cont)

print("[" + print_numbers + "]")
