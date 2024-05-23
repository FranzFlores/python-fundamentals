list = [21,32,42,34,55]

try: 
    print("#####Buscar elemento en una lista #####")
    finder = int(input("Ingrese un número: "))
    
    comprobe = isinstance(finder, int)
    while not comprobe or finder <= 0:
        finder = int(input("Ingrese un número: "))

    search = list.index(finder)
    print(f"El número {finder} está en la lista en la posición {search}")
except:
    print("El número no está en la lista")