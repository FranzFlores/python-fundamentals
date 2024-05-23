#Capturar excepcioenes y manejar errores en código 

"""
try:
    name = input("¿Cómo te llamas? ")

    if len(name) > 1:
        user_name = "El nombre es " + name

    print(user_name)
except:
    #Error al no ingresar nombre
    print("No se ingreso un nombre")
else:
    #Si todo ha ido bien
    print("Todo bien")
finally:
    print("Se terminó el programa")
"""

#multiples excepciones
""" 
try:
    number = int(input("Ingrese un número: "))
    print("El cuadrado del número es: ", number ** 2)
except TypeError:
    print("Se debe convertir a enteros los valores ingresados")
# except ValueError:
#     print("Se debe ingresar un número")
except Exception as e:
    print("Ha ocurrido un error: ", type(e).__name__)
"""

#Excepciones personalizadas 
try: 
    name = input("¿Cómo te llamas? ")
    age = int(input("¿Cuántos años tienes? "))

    if age < 5 or age > 110:
        raise ValueError("No es una edad válida")
    elif len(name) <=1:
        raise ValueError("No es un nombre válido")
    else:
        print("Bienvenido", name)
except ValueError:
    print("Introduce los datos correctamente")