class Car:
    # Atributos o propiedades
    color = ''
    mark = ''
    model = ''
    year = 0
    doors = 0
    velocity = 0
    
    #Propiedad privada
    __private = "Atributo privado"


    #Constructor
    def __init__(self, color, mark, model, year, doors, velocity):
        self.color = color
        self.mark = mark
        self.model = model
        self.year = year
        self.doors = doors
        self.velocity = velocity
        

    # Métodos Getter y Setter
    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_mark(self, mark):
        self.mark = mark

    def get_mark(self):
        return self.mark
    
    def get_private(self):
        return self.__private

    #Métodos de la clase
    def accelerate(self):
        self.velocity += 1

    def brake(self):
        self.velocity -= 1

    def getInfo(self):
        info = "-----Información del vehículo-----"
        info += "\nColor: " + self.color
        info += "\nMarca: " + self.mark
        info += "\nModelo: " + self.model
        info += "\nAño: " + str(self.year)
        info += "\nNúmero de puertas: " + str(self.doors)
        info += "\nVelocidad: " + str(self.velocity)
        return info

# Fin definicion de clase