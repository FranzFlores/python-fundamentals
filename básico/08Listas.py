"""
Listas (Arrays)
Son colecciones de datos bajo un único nombre.

Tuplas
Son colecciones de datos que no se pueden modificar.
"""

#Definir una lista
movies = ['Batman', 'Spiderman', 'Superman', 'Ironman']
singers = list(('Santana', 'Reik', 'Ricardo Arjona')) # Con tuplas
years = list(range(2000,2020)) # Con rangos
multiple = ["Franz",30,4.4,True] # Con diferentes tipos de datos

# Indices
print(movies[1]) #Inprime Spiderman
print(movies[-3]) #Inprime Spiderman (Cuenta de derecha a izquierda)
print(singers[1:3]) #Inprime un rango de indices (De 1 a 3)
print(singers[1:]) #Inprime un rango de indices (De 1 en adelante)

movies[0] = 'Batman Begins' # Cambia el valor de Batman

#Agregar elementos
singers.append("Maná") # Agrega un elemento al final de la lista
print(singers)

#Recorrer listas
#Con un bucle for
new_movie = ""
while new_movie != "STOP":
    new_movie = input("Ingrese una pelicula: ")
    if new_movie != "STOP":
        movies.append(new_movie)

for movie in movies:
    print(f"{movie.index(movie)+ 1}: {movie}")


#Listas multidimensionales
print("*******LISTADO DE CONTACTOS*******")
contactos = [
    ['Franz','franz@gmail.com'],
    ['Andrés','andres@gmail.com'],
    ['Luis','luis@gmail.com']
]

for contacto in contactos:
    for elemento in contacto:
        print(elemento) 
    print("\n")

# Funciones Predefinidas de las listas
players = ["Rafael", "Andres", "Luis"]
numbers = [1,2,5,8,3,4]

#Ordenar listas
numbers.sort()
print(numbers)

#Agregar elementos a una lista
numbers.append("Franz")
numbers.insert(0, "Andres") #Agrega un elemento una posición especifica

#Eliminar elementos de una lista
numbers.pop(3) #Elimina el elemento en la posicion 3
numbers.remove(4) #Elimina el elemento 4

# Cambiar el orden de los elementos al sentido contrario
numbers.reverse()

# Buscar en un lista
print('Andres' in players) # Devuelve un booleano

#Contar elementos 
len(players) #Devuelve la cantidad de elementos

# Contar las veces que esta el elemento dentro de la lista
players.count('Andres')

#Unir listas
players.extend(numbers)