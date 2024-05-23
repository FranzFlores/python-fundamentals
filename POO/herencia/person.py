class Person:

    def __init__(self, name, lastname, height, age): 
        self.name = name
        self.lastname = lastname
        self.height = height
        self.age = age

    #Metodos Getter y Setter
    def get_name(self):
        return self.name
    
    def get_lastname(self):
        return self.lastname
    
    def get_height(self):
        return self.height
    
    def get_age(self):
        return self.age
    
    def set_name(self, name):
        self.name = name
    
    def set_lastname(self, lastname):
        self.lastname = lastname
    
    def set_height(self, height):
        self.height = height

    def set_age(self, age):
        self.age = age

    #Metodos de la clase
    def talk(self):
        return "Estoy hablando"
    
    def walk(self):
        return "Estoy caminando"
    