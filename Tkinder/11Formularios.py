from tkinter import *

window_form = Tk()
window_form.geometry("800x500")

header = Label(window_form, text="Formulario 2")
header.config(
    padx=15,
    pady=15,
    fg="#ffffff",
    bg="green",
    font=("Consolas", 20)
)
header.grid(row=0, column=0, columnspan=5, sticky=W)

# botones Check
developer = IntVar()
student = IntVar()


def showProfession():
    text = ""

    if developer.get() == 1:
        text += "Desarrolador"
    if student.get() == 1:
        if developer.get() == 1:
            text += " y Estudiante"
        else:
            text += "Estudiante"

    show.config(text=text, bg="green", fg="white")


Label(window_form, text="A qué te dedicas?").grid(row=1, column=0)
Checkbutton(window_form, text="Programador", variable=developer,
            onvalue=1, offvalue=0, command=showProfession).grid(row=2, column=0)
Checkbutton(window_form, text="Estudiante", variable=student,
            onvalue=1, offvalue=0, command=showProfession).grid(row=3, column=0)

show = Label(window_form)
show.grid(row=4, column=0)


# Radios Buttons
option = StringVar()
option.set(None)

def check():
    selected.config(text=option.get())


Label(window_form, text="Cuál es tu genero?").grid(row=5)
Radiobutton(window_form, text="Masculino",
            variable=option, command=check, value="Masculino").grid(row=6)
Radiobutton(window_form, text="Femenino",
            variable=option, command=check, value="Femenino").grid(row=7)

selected = Label(window_form)
selected.grid(row=8)

# Menu de Opciones
opt = StringVar()
opt.set("Opción 1")

def selectOption():
    result.config(text=opt.get())

Label(window_form, text="Selecciona una opción").grid(row=5, column=1)
select = OptionMenu(window_form, opt, "Opción 1", "Opción 2", "Opción 3").grid(row=6, column=1)

Button(window_form, text="Seleccionar", command=selectOption).grid(row=7, column=1)

result = Label(window_form)
result.grid(row=8, column=1)

window_form.mainloop()
