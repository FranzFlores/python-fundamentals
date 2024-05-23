# Programación Orientada a Objetos

#Definir una clase: Molde para crear objetos
class Car:
    #Atributos o propiedades
    color = 'Rojo'
    mark = 'Toyota'
    model =  'Corolla'
    year = 2018
    doors = 4
    velocity = 100

    #Métodos, son acciones que podemos realizar (Funciones)
    def accelerate(self):
        self.velocity += 1
    
    def brake(self):
        self.velocity -= 1

    def get_velocity(self):
        return self.velocity

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color
#Fin definicion de clase

car = Car()
car.set_color('Azul')
print(car.mark, car.get_color())

print("Velocidad del coche", car.get_velocity())

car.accelerate()
car.accelerate()
car.accelerate()
print("Velocidad del coche", car.get_velocity())

car.brake()
print("Velocidad del coche", car.get_velocity())

print("---------------------")	

#Crear más objetos
car2 = Car()
print("Carro 2: ")

car2.set_color("Verde")
print(car2.mark,car2.get_color())