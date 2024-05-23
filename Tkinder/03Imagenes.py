from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("600x600")

# Agregar texto a la ventana
text = Label(window, text="Bienvenido al ejemplo de imágenes").pack(anchor=W)

# Agregar imagen a la ventana
image = Image.open("Tkinder/images//vengadores.jpg")
render = ImageTk.PhotoImage(image)

Label(window, image=render).pack()

window.mainloop()