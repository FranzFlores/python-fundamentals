from io import open
import pathlib
import shutil #Gestionar archivos
import os #Eliminar archivos

#Abrir archivo
path = str(pathlib.Path().absolute()) + "\\básico\\sistema_ficheros\\fichero_texto.txt"
file = open(path, "a+")

#Escribir en archivo
file.write("***********Texto escrito en archivo***********\n")

#Cerrar archivo
file.close()

#Abrir archivo de lectura
path = str(pathlib.Path().absolute()) + "\\básico\\sistema_ficheros\\fichero_texto.txt"
file_read = open(path, "r")

#Leer contenido de archivo
# content = file_read.read()
# print(content)

#Leer contenido y guardar en lista
list = file_read.readlines()
print(list)

for line in list:
    print(line.center(20))

file_read.close()

#Copiar Archivo
"""
original_path = str(pathlib.Path().absolute()) + "\\básico\\sistema_ficheros\\fichero_texto.txt"
new_path = str(pathlib.Path().absolute()) + "\\básico\\sistema_ficheros\\fichero_texto_copia.txt"
shutil.copyfile(original_path, new_path) 
""" 

#Mover Archivo
"""
original_path = str(pathlib.Path().absolute()) + "\\básico\\sistema_ficheros\\fichero_texto_copia.txt"
new_path = str(pathlib.Path().absolute()) + "\\básico\\sistema_ficheros\\fichero_texto_movido.txt"

shutil.move(original_path, new_path)
"""

#Eliminar archivo
"""
new_path = str(pathlib.Path().absolute()) + "\\básico\\sistema_ficheros\\fichero_texto_movido.txt"
os.remove(new_path)
"""

#Comprobar existencia de archivo
import os.path
new_path = str(pathlib.Path().absolute()) + "\\básico\\sistema_ficheros\\fichero_texto_movido.txt"
if os.path.isfile(new_path):
    print("El archivo existe")
else: 
    print("El archivo no existe")

