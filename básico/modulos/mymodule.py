def helloWorld(name):
    return f"Hola Mundo, mi nombre es {name}"

def calculator(num1,num2, op = False):
    add = num1 + num2
    subtraction = num1 - num2
    string_print = ""
    string_print += f"Suma: {num1} + {num2} = {add}\n" 
    string_print += f"Resta: {num1} - {num2} = {subtraction}\n" 

    if op:
        multiplication = num1 * num2
        division = num1 / num2
        string_print += f"Multiplicación: {num1} * {num2} = {multiplication}\n"
        string_print += f"División: {num1} / {num2} = {division}\n"

    return string_print