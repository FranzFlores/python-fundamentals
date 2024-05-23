"""
Ejercicio 3: Programa que compruebe si una variable está vacía y si lo está rellenarla con un mensaje en minusculas y mostrarla en mayúsculas. 
"""

variable = input("Ingrese una variable: ")

if variable:
    print(variable.upper())
else: 
    variable = ("Texto de Prueba").lower()
    print(variable.upper())

print(f"El Valor de variable es: {variable}")