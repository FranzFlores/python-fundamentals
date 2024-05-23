"""
Ejercicio 9. Hacer un programa que pida numeros al usuario indefinidamente hasta que el usuario ingrese el numero 111.
"""

while True:
    num = int(input("Ingrese un número: "))
    if num == 111:
        break
    print(f"El número ingresado es {num}")