"""
Proyecto Python y Mysql:
- Abrir Asistente
- Login o registro
- Si se elige registro, crear un usuario en BBDD
- Si se elige login, validar usuario y contraseña
 - Permitir Gestionar notas 
"""

from users import actions

print(""" 
Acciones disponibles:
- Registrar (1)
- Iniciar sesión (2)
""")

actions_object = actions.Actions()
action = int(input("¿Qué quieres hacer? "))

if action == 1:
    actions_object.signup_messages()
elif action == 2:
    actions_object.login_messages()