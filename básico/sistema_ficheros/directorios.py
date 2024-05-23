import os
import pathlib, shutil

# Crear carpeta
if not os.path.isdir("./carpeta"):
    os.mkdir("./carpeta")
else:
    print("La carpeta ya existe")

# Eliminar carpeta
# os.rmdir("./carpeta")

# Copiar carpeta
"""
original_path = str(pathlib.Path().absolute()) + "\\básico\\sistema_ficheros\\carpeta"
new_path = str(pathlib.Path().absolute()) + "\\básico\\sistema_ficheros\\carpeta_copia"

shutil.copytree(original_path, new_path)
"""

print("Contenido de la carpeta:")
content = os.listdir('./carpeta')
print(content)
