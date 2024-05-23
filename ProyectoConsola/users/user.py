import datetime
import hashlib
import users.connection as connection

#Conectar a la base de datos
connect = connection.connect()
database = connect[0]
cursor = connect[1]

class User:

    def __init__(self, name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password

    # Devuelve 1 si el usuario se ha registrado correctamente.
    def signup(self):
        date = datetime.datetime.now()

        # Cifrar la contraseña
        password_hash = hashlib.sha256()
        password_hash.update(self.password.encode('utf-8')) # encode('utf-8') Convierte el string  en bytes

        sql = 'INSERT INTO users (name, lastname, email, password, date) VALUES (%s, %s, %s, %s,%s)'
        user = (self.name, self.lastname, self.email, password_hash.hexdigest(), date)

        try :
            cursor.execute(sql, user)
            # Ejecutar el commit para guardar los cambios
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result


    #Registro de usuario 
    def login(self):
        #Consulta para obtener el usuario
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"

         # Cifrar la contraseña
        password_hash = hashlib.sha256()
        password_hash.update(self.password.encode('utf-8'))

        #Datos para la consulta
        user = (self.email, password_hash.hexdigest())

        cursor.execute(sql, user)
        result = cursor.fetchone()

        return result