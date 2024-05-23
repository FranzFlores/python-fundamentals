"""
Ejercicio 6: Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el título de la tabla y después los resultados de las operaciones.
"""

for i in range(1,11):
    print("\nTabla del " + str(i))
    for j in range(1,11):
        print(str(i) + " x " + str(j) + " = " + str(i*j))