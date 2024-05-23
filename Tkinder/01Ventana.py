# Tkinder: Modulo para crear interfaces graficas en Python

from tkinter import *
import os.path

class Program:
    
    def __init__(self):
        self.title = "Tkinder Ventanas"
        self.icon = "images/camara.ico"
        self.icon_alt = "Tkinder/images/camara.ico"
        self.size = "500x500"
        self.resizable = False

    def load(self):
        #Crear la ventana principal
        window = Tk()
        self.window = window

        #Comprobar si existe una imagen
        path_icon = os.path.abspath(self.icon)

        if not os.path.isfile(path_icon):
            path_icon = os.path.abspath(self.icon_alt)


        #Icono de la ventana
        window.iconbitmap(path_icon)

        #Titulo de la ventana
        window.title(self.title)

        #Mostrar texto en el programa
        text = Label(window, text=path_icon)
        text.pack()

        #Cambiar el tamaño de la ventana
        window.geometry(self.size)

        #Bloquear el tamaño de la ventana
        if self.resizable:
            window.resizable(1, 1)
        else:
            window.resizable(0,0)
    

    def add_text(self, info):
        text = Label(self.window, text=info)
        text.pack()

    def show_window(self):
        self.window.mainloop()

#instanciar la clase
program = Program()
program.load()
program.add_text("Liga de Quito")
program.show_window()