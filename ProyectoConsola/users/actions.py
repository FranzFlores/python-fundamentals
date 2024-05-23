import users.user as model
import tasks.actions as note

class Actions:

    # Mensajes de Registro en el sistema
    def signup_messages(self):
        print("\nRegistro del Sistema")
        name = input("Nombre: ")
        lastname = input("Apellidos: ")
        email = input("Email: ")
        password = input("Contraseña: ")

        user = model.User(name, lastname, email, password)
        signup = user.signup()

        if signup[0] >= 1:
            print("\nRegistro exitoso")
            print("\nBienvenido {} {}".format(signup[1].name, signup[1].lastname))
        else:
            print("\nError al registrar")
    

    #Mensajes de inicio de sesión
    def login_messages(self):
        print("\nInicio de sesión")

        try: 
            email = input("Email: ")
            password = input("Contraseña: ")

            user = model.User(None, None, email, password)
            login = user.login()

            if email == login[3]:
                print("\nBienvenido {} {}".format(login[1], login[2]))
                self.nextActions(login)

        except Exception as e:
            print(e)
            print("\nError al iniciar sesión")
    

    # Mensajes cuando las credenciales son correctas 
    def nextActions(self, user):
        print("""\n
        Acciones disponibles:
        - Crear Nota (1)
        - Mostrar tus Notas (2)
        - Eliminar Nota (3)
        - Salir (4)
        """)

        option = int(input("¿Qué quieres hacer? "))
        action = note.Actions()


        if option == 1:
            print("\nCrear Nota")
            action.create(user)
            self.nextActions(user)
        elif option == 2:
            print("\nMostrar tus notas")
            action.list_notes(user)
            self.nextActions(user)
        elif option == 3:
            print("\nEliminar Nota")
            action.delete(user)
            self.nextActions(user)
        elif option == 4:
            print("\nHasta Pronto")
            exit()
        

        