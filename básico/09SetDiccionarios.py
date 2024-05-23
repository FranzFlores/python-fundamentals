"""
SET es un tipo de dato, para tener una colección de valores pero no se tiene ni índice ni orden.
"""

people = {'Alice', 'Bob', 'Carol', 'Dave'}
people.add("Franz")
print(people)


"""
Diccionario: Es un tipo de dato almacena pares de clave-valor similar a un JSON
"""
person = {
    "name": "Franz",
    "lastname": "Flores",
    "age": "30"
}

print(person['lastname'])


""" 
Lista con diccionarios
"""
contacts = [{
    "name": "Franz",
    "email": "franz@gmail.com"
},
    {
    "name": "Juan",
    "email": "juan@gmail.com"
}]

print(contacts[0]['name'])

for contact in contacts:
    print(f"El contacto es: {contact['name']}")