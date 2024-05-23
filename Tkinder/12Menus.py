from tkinter import *

window= Tk()
window.geometry("600x600")

my_menu=Menu(window)
window.config(menu=my_menu)

file = Menu(my_menu, tearoff=0)
file.add_command(label="Nuevo archivo")
file.add_command(label="Abrir archivo")
file.add_separator()
file.add_command(label="Guardar")
file.add_separator()
file.add_command(label="Salir", command=window.quit)

my_menu.add_cascade(label="Archivo", menu=file)
my_menu.add_command(label="Editar")
my_menu.add_command(label="Ayuda")

window.mainloop()
