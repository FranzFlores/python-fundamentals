"""
Ejercicio 4. Pedir dos numeros al usuario y realizar las operaciones básicas con ellos.
"""

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

print("#######OPERACIONES BÁSICAS#######")
print(f"La suma es {num1 + num2}")
print(f"La resta es {num1 - num2}")
print(f"La multiplicación es {num1 * num2}")
print(f"La división es {num1 / num2}")

print("#######OPERACIONES AVANZADAS#######")
print(f"El cuadrado del primer número es {num1**2}")
print(f"El cuadrado del segundo número es {num2**2}")
print(f"La raíz cuadrada del primer número es {num1**(1/2)}")
print(f"La raíz cuadrada del segundo número es {num2**(1/2)}")