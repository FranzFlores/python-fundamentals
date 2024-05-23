from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Formularios")
window.config(
    bd=50,  # Borde transparente
)


def getData():
    result.set(data.get())

    if len(result.get()) > 1:
        label_show.config(
            bg="green",
            fg="white",
        )


data = StringVar()
result = StringVar()

Label(window, text="Ingresar un texto:").pack(anchor=NW)
Entry(window, textvariable=data).pack(anchor=NW)

Label(window, text="Dato Recogido").pack(anchor=NW)
label_show = Label(window, textvariable=result)
label_show.pack(anchor=NW)

Button(window,
       text="Mostrar Dato",
       command=getData  # Funcion que se ejecuta al hacer click
       ).pack(anchor=NW)

window.mainloop()
