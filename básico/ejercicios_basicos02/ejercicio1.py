"""
Ejercicio 1. Hacer un programa que tenga una lista de 8 números enteros y haga lo siguiente:
- Recorrer la lista y mostrar los elementos.
- Hacer una función que recorra la lista y devuelva una cadena con los elementos separados por coma.
- Ordenarla y mostrarla 
- Mostrar su longitud
- Buscar un elemento (El usuario pida por teclado)
"""

#Definir lista
numbers = [2,3,5,6,7,8,1,4]

#Recorrer lista
for number in numbers:
    print(number)

#Función que recorre la lista y devuelve una cadena con los elementos separados por coma.
def list_to_string(lista):
    cadena = ""
    for number in lista:
        cadena += str(number) + ","
    return "[" + cadena + "]"
print(list_to_string(numbers))

#Ordenar lista
numbers.sort()
print(numbers)

#Mostrar su longitud
print(len(numbers))

#Buscar un elemento que el usuario pida por teclado
finder = int(input("Ingrese un número: "))
for number in numbers: 
    if number == finder:
        print(f"El número {finder} está en la lista")
        break
else: 
    print(f"El número {finder} no está en la lista")
