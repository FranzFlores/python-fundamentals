"""
Ejercicio 8: Hacer un programa que obtenga un porcentaje de una cantidad ingresada por el usuario.
"""

num = int(input("Ingrese un número: "))
percent = int(input("Ingrese el porcentaje: "))

print(f"El {percent}% de {num} es {num*percent/100}")