"""
Ejercicio 10. Pedir la nota de 15 alumnos y sacar por pantalla cuantos han reprobado y cuantos han aprobado.
"""
cont = 1
passed = 0
failed = 0

while cont <= 15:
    grade = int(input("Ingrese la nota del estudiante " + str(cont) + ": "))
    if grade >= 7:
        passed += 1
    else: 
        failed += 1
    cont+=1

print(f"Los estudiantes que aprobaron son {passed} y los que reprobaron son {failed}")