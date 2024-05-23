"""
Ejercicio 5. Crear una lista con el contenido de esta tabla:
Baladas                     Rock                    Pop
Mariposas                   Crazy                   Te Quiero
Me dedique a perderte       Criyn'                  Ave Maria
Vuelve                      Entre dos tierras       Acuerdate

Mostrar Ordenada por Genero
"""

data = [
    {
        "name": "Baladas",
        "songs": ["Mariposas","Me dedique a perderte","Vuelve"]
    },
    {
        "name": "Rock",
        "songs": ["Crazy","Criyn'","Entre dos tierras "]
    },
    { 
        "name": "Pop",
        "songs": ["Te Quiero","Ave Maria","Acuerdate"]
    }
]


for gender in data:
    print(f"Categoría: { gender['name']} ")
    for song in gender['songs']:
        print(song)        