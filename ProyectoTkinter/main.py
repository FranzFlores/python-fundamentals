"""
Crear un programa que tenga:
- Ventana
- Tamaño Fijo
- No redimensionable
- Un Menu (Inicio, Agregar, Informacion, Salir)
- Diferentes Pantallas
- Formulario de agregar productos
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla principal
- Opcion de salir
"""
from tkinter import *
from tkinter import ttk

window = Tk()

# Caracteristicas de la ventana
# window.geometry("500x500")
window.minsize(500, 500)
window.title("Proyecto Tkinter")
window.resizable(0, 0)  # No se puede redimensionar

# Variables
name_data = StringVar()
price_data = StringVar()
products = []


def add_products():
    products.append([name_data.get(), price_data.get(),
                    add_description_entry.get("1.0", "end-1c")])
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)

    home()


# Pantallas
# Campos de Pantalla (INICIO)
home_label = Label(window, text="Inicio")
# products_box = Frame(window)
Label(window).grid(row=1, column=0)

products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
products_box.heading("#0", text="Producto", anchor=W)
products_box.heading("#1", text="Precio", anchor=W)

# Campos de Pantalla (AGREGAR)
add_frame = Frame(window, width=250)
add_label = Label(add_frame, text="Agregar Producto")

add_name_label = Label(add_frame, text="Nombre:")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio:")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Descripción:")
add_description_entry = Text(add_frame)

add_separator = Label(add_frame)

button = Button(add_frame, text="Guardar", command=add_products)


# Campos de Pantalla (INFORMACION)
info_label = Label(window, text="Información")
data_label = Label(window, text="Creado por Franz Flores")


def home():
    # Encabezado
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=210,
        pady=20
    )
    home_label.grid(row=0, column=0, columnspan=4)

    products_box.grid(row=2)

    # Listar Productos
    # for product in products:
    #     if len(product) == 3:
    #         product.append("added")
    #         Label(products_box, text=product[0]).grid()
    #         Label(products_box, text=product[1]).grid()
    #         Label(products_box, text=product[2]).grid()
    #         Label(products_box, text="---------------------------").grid()

        # Listar Productos
    for product in products:
        if len(product) == 3:
            product.append("added")
            products_box.insert("", 0, text=product[0], values=product[1])

    

    # Ocultar Pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True


def add():
    # Encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=120,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=4)

    # Campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_description_entry.grid(row=3, column=1, sticky=W)
    add_description_entry.config(
        width=30, height=5, padx=15, pady=15)

    add_separator.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    button.grid(row=5, column=1, sticky=NW)
    button.config(padx=15, pady=5, bg="green", fg="white")

    # Ocultar Pantallas
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()

    return True


def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=150,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    # Ocultar Pantallas
    home_label.grid_remove()
    add_label.grid_remove()
    add_frame.grid_remove()
    products_box.grid_remove()

    return True


# Cargar Pantallas
home()

# Menu Superior
menu_top = Menu(window)
menu_top.add_command(label="Inicio", command=home)
menu_top.add_command(label="Agregar", command=add)
menu_top.add_command(label="Informacion", command=info)
menu_top.add_command(label="Salir", command=window.quit)

window.config(menu=menu_top)

window.mainloop()
