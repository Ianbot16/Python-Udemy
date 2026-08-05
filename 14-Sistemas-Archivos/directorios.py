import os
import shutil

#Crear una carpeta
if not os.path.exists("./14-Sistemas-Archivos/mi_carpeta"):
    os.mkdir("./14-Sistemas-Archivos/mi_carpeta")
else:
    print("La carpeta ya existe")

#Eliminar una carpeta
#os.rmdir("./14-Sistemas-Archivos/mi_carpeta_copiada")

#Copiar
"""
ruta_origen = "./14-Sistemas-Archivos/mi_carpeta"
ruta_nueva = "./14-Sistemas-Archivos/mi_carpeta_copiada"
shutil.copytree(ruta_origen, ruta_nueva)
"""

print("Contenido de la carpeta actual:")
contenido = os.listdir("./14-Sistemas-Archivos/mi_carpeta")

for fichero in contenido:
    print("Fichero:", fichero)