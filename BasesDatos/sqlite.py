#Importar modulo
import sqlite3

#Crear conexion
connection = sqlite3.connect('./BasesDatos/ejemplo.db')

#Crear tabla
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Usuarios("+
    "id INTEGER PRIMARY KEY AUTOINCREMENT ," +
    "nombre VARCHAR(255),"+  
    "apellido VARCHAR(255),"+ 
    "edad INTEGER)")
#Guardar cambios
connection.commit()

#Insertar datos
cursor.execute("INSERT INTO Usuarios(nombre, apellido, edad) VALUES('Emilio', 'Flores', 22)")
connection.commit()

#Leer datos
cursor.execute("SELECT * FROM Usuarios;")
users = cursor.fetchall()

for user in users:
    print("Id:", user[0])
    print("Nombre: ", user[1])
    print("Apellido: ", user[2])
    print("Edad: ", user[3])
    print("\n")

cursor.execute("SELECT * FROM Usuarios;")
user = cursor.fetchone()

#Borrar registro
cursor.execute("DELETE FROM Usuarios WHERE id = 1;")
connection.commit()

#Insertar registros multiples
users_insert = [
    ("Juan", "Perez", 23),
    ("Pedro", "Perez", 23),
    ("María", "Perez", 23),
]

cursor.executemany("INSERT INTO Usuarios(nombre, apellido, edad) VALUES(?, ?, ?)", users_insert)
connection.commit()

#Actualizar registro
cursor.execute("UPDATE Usuarios SET edad = 24 WHERE id = 2;")
connection.commit()

#Cerrar conexion
connection.close()