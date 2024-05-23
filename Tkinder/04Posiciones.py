from tkinter import *

window = Tk()
window.geometry("600x600")

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


text1 = Label(window, text="Texto de prueba 1")
text1.config(
    justify=RIGHT, # Justificar texto a la derecha
    width=40, # Tamano del contenedor del texto
    height=10,     # Tamano del contenedor del texto
    bg="green" # Color de fondo
)
text1.pack(
    side=TOP, # Posicionar texto en la parte superior
    fill=X, # Rellenar todo el espacio disponible
    expand=YES # Expandir el espacio disponible
)

text2 = Label(window, text="Texto de prueba 2")
text2.config(
    justify=RIGHT, # Justificar texto a la derecha
    width=40, # Tamano del contenedor del texto
    height=10,     # Tamano del contenedor del texto
    bg="red" # Color de fondo
)
text2.pack(
    side=LEFT # Posicionar texto a la izquierda
)

text3 = Label(window, text="Texto de prueba 3")
text3.config(
    justify=RIGHT, # Justificar texto a la derecha
    width=40, # Tamano del contenedor del texto
    height=10,     # Tamano del contenedor del texto
    bg="blue" # Color de fondo
)
text3.pack(
    side=LEFT # Posicionar texto a la izquierda
)

window.mainloop()


