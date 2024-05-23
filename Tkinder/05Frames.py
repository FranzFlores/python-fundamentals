from tkinter import *

window = Tk()
window.title("Ejercicio de Frames")
window.geometry("500x500")

# Crear y dar estilo al marco de la ventana
frame = Frame(window, width=50, height=50)
frame.config(
    bg="blue",  # Color de fondo
    bd=5,  # Borde
    relief=SOLID  # Estilo del borde
)
frame.pack(
    side=RIGHT, # Posicionar el marco a la derecha
    anchor=SE # Posicionar el marco en el extremo inferior derecho
)


# Crear y dar estilo al marco de la ventana
frame1 = Frame(window, width=60, height=60)
frame1.config(
    bg="green",  # Color de fondo
    bd=5,  # Borde
    relief=SOLID  # Estilo del borde
)
frame1.pack(
    side=LEFT, # Posicionar el marco a la derecha
    anchor=NW # Posicionar el marco en el extremo inferior derecho
)

# Crear y dar estilo al marco de la ventana
frame2 = Frame(window, width=60, height=60)
frame2.config(
    bg="orange",  # Color de fondo
    bd=5,  # Borde
    relief=SOLID  # Estilo del borde
)
frame2.pack(
    side=LEFT, # Posicionar el marco a la derecha
    anchor=NW # Posicionar el marco en el extremo inferior derecho
)

frame_parent = Frame(window, width=70, height=70)
frame_parent.config(
    bg="yellow",  # Color de fondo
    bd=5,  # Borde
    relief=SOLID  # Estilo del borde
)
frame_parent.pack(
    side=RIGHT, # Posicionar el marco a la derecha
    anchor=NW, # Posicionar el marco en el extremo inferior derecho
    fill=BOTH, # Rellenar todo el espacio disponible
    expand=YES
)
frame_parent.pack_propagate(False) #evita que el marco se ajuste al contenido
text = Label(frame_parent, text="Marco Padre")
text.config(
    bg="red",  # Color de fondo
    fg="white",  # Color de letra
    font=("Arial", 20, "bold"),    
    anchor=CENTER,
    bd=2,
    relief=SOLID
)
text.pack(fill=Y, expand=YES)


# Crear y dar estilo al marco de la ventana
frame3 = Frame(frame_parent, width=30, height=30)
frame3.config(
    bg="lightblue",  # Color de fondo
    bd=5,  # Borde
    relief=SOLID  # Estilo del borde
)
frame3.pack(
    side=RIGHT, # Posicionar el marco a la derecha
    anchor=SW # Posicionar el marco en el extremo inferior derecho
)



window.mainloop()
