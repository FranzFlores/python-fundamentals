"""
for variable in elemento_iterable (lista, tupla, diccionario, etc)
"""

# Bucle for
contador = 0
resultado = 0
for contador in range(0, 5):
    resultado += contador

print(f"El resultado es {resultado}")

# Ejemplo con tablas de multiplicar
num = int(input("Introduce un número psra obtener su tabla de multiplicar: "))

if num < 1:
    num = 1

print(f"\n### Tabla de multiplicar del {num} ###")

for numero_tabla in range(1,11):
    
    if num == 45:
        print("No se puede obtener el numero")
        break

    print(f"{num} x {numero_tabla} = {num*numero_tabla}")
else: 
    print("Fin de tabla")


## bucle while
cont = 1
imprimir = str(0)
while cont <= 10:
    imprimir = imprimir + ", " + str(cont)
    cont += 1
print(imprimir)


## Ejemplo con bucle while
numero = int(input("Introduce un número: "))

if numero < 1:
    numero = 1

print(f"\n### Tabla de multiplicar del {num} ###")
cuenta = 1
while cuenta <= 10:
    print(f"{numero} x {cuenta} = {numero*cuenta}")
    cuenta += 1
else: 
    print("Fin de tabla")