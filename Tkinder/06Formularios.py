from tkinter import *
from turtle import st

window = Tk()
window.title("Ejercicio de Formulario | Curso Python")
window.geometry("700x400")


# Texto Encabezado
header = Label(window, text="Formulario de Registro | Curso Python")
header.config(
    fg="white",
    bg="darkgray",
    font=("Opens Sans", 18),
    padx=10,
    pady=10
)
header.grid(row=0, column=0, columnspan=12, sticky=W)
# header.pack(side=LEFT, anchor=N, fill=X, expand=True)

# Texto para el campo (nombre)
label_name = Label(window, text="Nombre")
label_name.grid(row=1, column=0, padx=5, pady=5)

# Campos de Texto (Nombre)
input_text = Entry(window)
input_text.grid(row=1, column=1, sticky=W, padx=5, pady=5)
# input_text.config(justify="left", state="normal")

# Texto para el campo (apellidos)
label_name = Label(window, text="Apellidos")
label_name.grid(row=2, column=0, padx=5, pady=5)

# Campos de Texto (apellidos)
input_text = Entry(window)
input_text.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Texto para el textarea (descripcion)
label_name = Label(window, text="Descripción")
label_name.grid(row=3, column=0, sticky=N, padx=5, pady=5)

# Textarea (descripcion)
textarea = Text(window)
textarea.grid(row=3, column=1)
textarea.config(width=40, height=6, font=("Arial", 12), padx=5, pady=5)

#Botones
Label(window).grid(row=4, column=1)

btn = Button(window, text="Enviar")
btn.grid(row=4, column=1, sticky=W)
btn.config(padx=15, pady=15, bg="Green", fg="white", font=("Arial", 12))

window.mainloop()
