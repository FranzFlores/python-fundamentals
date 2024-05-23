"""
CALCULADORA:
- Dos campos de texto
- 4 Botones para las operaciones
- Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("Calculadora")
window.geometry("400x400")
window.config(
    bd=25,  # Borde transparente
    bg="#212121"
)

# Encabezado
header = Label(window, text="Calculadora")
header.config(
    bg="#212121",
    fg="#ffffff",
    font=("Opens Sans", 18),
    padx=10,
    pady=10
)
header.pack(anchor=N, fill=X, expand=True)

# Campos de texto
num1 = StringVar()
num2 = StringVar()
result = StringVar()

def parseToFloat(number):
    try:
        return float(number)
    except:
        messagebox.showerror("Error","Introduce bien los datos")
        return 0
      

#Funciones con las operaciones
def add():
    try:
        result.set(parseToFloat(num1.get()) + parseToFloat(num2.get()))
        showResult()
    except:
        messagebox.showerror("Error","Introduce bien los datos")

def subtract():

    result.set(parseToFloat(num1.get()) - parseToFloat(num2.get()))
    showResult()

def multiply():
    result.set(parseToFloat(num1.get()) * parseToFloat(num2.get()))
    showResult()

def divide():
    result.set(parseToFloat(num1.get()) / parseToFloat(num2.get()))
    showResult()

def showResult():
    messagebox.showinfo("Resultado", f"El resultado de la operación es {result.get()}")
    num1.set("")
    num2.set("")


frame_form = Frame(window, width=350, height=200)
frame_form.config(
    bd=5,
    relief=SOLID,
    padx=15,
    pady=15
)
frame_form.pack(side=TOP, anchor=CENTER)
frame_form.pack_propagate(False)


# Etiqueta y campo de texto para el primer numero
label_num1 = Label(frame_form, text="Numero 1:", justify="center").pack()
input_num1 = Entry(frame_form, textvariable=num1).pack()

# Etiqueta y campo de texto para el segundo numero
label_num2 = Label(frame_form, text="Numero 2:", justify="center").pack()
input_num2 = Entry(frame_form, textvariable=num2).pack()

#Separador
Label(frame_form, text="").pack()

#Botones
Button(frame_form, text="Suma", command=add).pack(side=LEFT, fill=X, expand=True)
Button(frame_form, text="Resta", command=subtract).pack(side=LEFT, fill=X, expand=True)
Button(frame_form, text="Multiplicación", command=multiply).pack(side=LEFT, fill=X, expand=True)
Button(frame_form, text="División", command=divide).pack(side=LEFT, fill=X, expand=True)


window.mainloop()
