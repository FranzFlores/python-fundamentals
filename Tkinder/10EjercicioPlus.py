"""
CALCULADORA:
- Dos campos de texto
- 4 Botones para las operaciones
- Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox


class Calculator:

    def __init__(self,alerts):
        self.num1 = StringVar()
        self.num2 = StringVar()
        self.result = StringVar()
        self.alerts = alerts

    def parseToFloat(self, number):
        try:
            return float(number)
        except:
            messagebox.showerror("Error", "Introduce bien los datos")
            return 0

    # Funciones con las operaciones

    def add(self):
        try:
            self.result.set(self.parseToFloat(self.num1.get()) +
                            self.parseToFloat(self.num2.get()))
            self.showResult()
        except:
            messagebox.showerror("Error", "Introduce bien los datos")

    def subtract(self):
        try:
            self.result.set(self.parseToFloat(self.num1.get()) -
                            self.parseToFloat(self.num2.get()))
            self.showResult()
        except:
            messagebox.showerror("Error", "Introduce bien los datos")

    def multiply(self):
        try:
            self.result.set(self.parseToFloat(self.num1.get())
                            * self.parseToFloat(self.num2.get()))
            self.showResult()
        except:
            messagebox.showerror("Error", "Introduce bien los datos")

    def divide(self):
        try:
            self.result.set(self.parseToFloat(self.num1.get())
                            / self.parseToFloat(self.num2.get()))
            self.showResult()
        except:
            messagebox.showerror("Error", "Introduce bien los datos")

    def showResult(self):
        self.alerts.showinfo(
            "Resultado", f"El resultado de la operación es {self.result.get()}")
        self.num1.set("")
        self.num2.set("")


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


frame_form = Frame(window, width=350, height=200)
frame_form.config(
    bd=5,
    relief=SOLID,
    padx=15,
    pady=15
)
frame_form.pack(side=TOP, anchor=CENTER)
frame_form.pack_propagate(False)

# Operaciones
calculator = Calculator(messagebox)

# Etiqueta y campo de texto para el primer numero
label_num1 = Label(frame_form, text="Numero 1:", justify="center").pack()
input_num1 = Entry(frame_form, textvariable=calculator.num1).pack()

# Etiqueta y campo de texto para el segundo numero
label_num2 = Label(frame_form, text="Numero 2:", justify="center").pack()
input_num2 = Entry(frame_form, textvariable=calculator.num2).pack()

# Separador
Label(frame_form, text="").pack()

# Botones
Button(frame_form, text="Suma", command=calculator.add).pack(
    side=LEFT, fill=X, expand=True)
Button(frame_form, text="Resta", command=calculator.subtract).pack(
    side=LEFT, fill=X, expand=True)
Button(frame_form, text="Multiplicación", command=calculator.multiply).pack(
    side=LEFT, fill=X, expand=True)
Button(frame_form, text="División", command=calculator.divide).pack(
    side=LEFT, fill=X, expand=True)

window.mainloop()
