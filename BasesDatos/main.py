import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="python"
)

#Cursor: Permite ejecutar consultas
cursor = database.cursor(buffered=True)

#Crear Base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS python")

#Mostrar las Base de datos
"""
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""

#Crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehiculos(
        id INT(10) AUTO_INCREMENT NOT NULL, 
        marca VARCHAR(255) NOT NULL,
        modelo VARCHAR(255) NOT NULL, 
        precio FLOAT(10,2) NOT NULL,
        CONSTRAINT pk_vehiculo PRIMARY KEY (id)
    )""")

#Mostrar tablas
cursor.execute("SHOW TABLES")

for tables in cursor:
    print(tables)

"""
#Insertar datos
cursor.execute("INSERT INTO vehiculos(marca, modelo, precio) VALUES('Ford', 'Focus', 10000)")

#Insertar varios datos
cars = [
    ("Ford", "4x4", 8000),
    ("Renault", "Clio", 5000),
    ("Chevrolet", "Zafira", 10000),
    ("Citroen", "Carro", 7000),
]   

cursor.executemany("INSERT INTO vehiculos(marca, modelo, precio) VALUES(%s, %s, %s)", cars)
"""

#Obtener datos
# cursor.execute("SELECT * FROM vehiculos") #Todos los datos
# cursor.execute("SELECT marca FROM vehiculos") #Solo una columna
cursor.execute("SELECT * FROM vehiculos WHERE precio > 9000 AND marca='Ford'") #Dos columnas

#Obtiene todos los registros
result = cursor.fetchall()

##Obtener un registro
# result = cursor.fetchone()

for car in result:
    print(car)

#Borrar registro
"""
cursor.execute("DELETE FROM vehiculos WHERE marca='Ford'")
print(cursor.rowcount, "Registros borrados")
"""

#Actualizar registro
cursor.execute("UPDATE vehiculos SET precio=5000 WHERE marca='Chevrolet'")
database.commit()