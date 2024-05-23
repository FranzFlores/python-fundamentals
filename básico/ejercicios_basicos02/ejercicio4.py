"""
Ejercicio 4. Crear un script que tenga 4 variables, una lista, un string, un entero y un booleano y que imprima un  
mensaje según el tipo de dato de cada variab le. Usar funciones
"""

list_example = [1,2,3]
text = "Hola"
integer_number = 1
boolean = True


def print_type(variable, type):
    result = ""
    if isinstance(variable, type):
        result = "La variable es del tipo: " + str(type)
    else:
        result = "La variable no es del tipo: " + str(type)
    return result

print(print_type(list_example, list))
