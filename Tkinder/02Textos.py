from tkinter import *

window = Tk()
window.geometry("500x500")

# Agregar texto a la ventana
text = Label(window, text="Bienvenido a Tkinder")

#Estilos del texto
text.config(
    fg="white", # Color de texto
    bg="black",  # Color de fondo
    padx=10,    # Margen izquierdo
    pady=10,    # Margen superior
    font=("Arial", 30), # Tipo de letra y tamaño
    cursor="hand2" # Cursor del mouse
)
text.pack()

# Parametros de palabra clave: Permite cambiar el orden de los parametros
def tests(name, lastname, country):
    return f"Hola {name} {lastname}, eres de {country}"

text1 = Label(window, text=tests("Franz", "Flores","Ecuador"))
text1.config(
    justify=RIGHT, # Justificar texto a la derecha
    width=40, # Tamano del contenedor del texto
    height=10,     # Tamano del contenedor del texto
    bg="orange" # Color de fondo
)
text1.pack(
    anchor=W # Justificar texto a la izquierda
)

window.mainloop()


