from car import Car

auto = Car("Rojo", "Toyota", "Corolla", 2018, 4, 100)
auto1 = Car("Azul", "Chevrolet", "Aveo", 2020, 3, 250)
auto2 = Car("Verde", "Ford", "Fiesta", 2019, 2, 150)
auto3 = Car("Blanco", "Ford", "Focus", 2020, 4, 200)

print(auto.getInfo())
# print(auto1.getInfo())
# print(auto2.getInfo())
# print(auto3.getInfo())

# Detectar Tipo
if type(auto) == Car:
    print("Es un objeto de la clase Car")
else:
    print("No es un objeto de la clase Car")

#Visibilidad de atributos
print("Mostrar atributo privado", auto.__private)