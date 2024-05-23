from tkinter import *
from tkinter import messagebox as MessageBox

window = Tk()
window.config(bd=70)

def showAlert():
    MessageBox.showinfo("Alerta", "Mensaje de la alerta")
    MessageBox.showwarning("Warning", "Mensaje de la alerta") # Warning
    MessageBox.showerror("Error", "Mensaje de la alerta") # Error

Button(window, text="Mostrar Alerta", command=showAlert).pack()

def exit(name):
    result = MessageBox.askquestion("Salir", "¿Desea salir de la aplicación?")

    if result == "yes":
        MessageBox.showinfo("Salir", f"Gracias por usar la aplicación {name}")
        window.destroy()


Button(window, text="Salir", command=lambda: exit("Franz Flores")).pack()
# lambda: Permite pasar un parametro a la funcion


window.mainloop()