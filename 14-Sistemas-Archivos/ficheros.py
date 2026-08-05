from io import open
import pathlib
import shutil

#Abrir archivo
ruta= str(pathlib.Path().absolute())+"/14-Sistemas-Archivos/fichero_texto.txt"
print(ruta)
archivo = open(ruta, "a+")

#Escribir
archivo.write("*****Soy un texto metido desde python*****\n")

#Cerrar el archivo
archivo.close()

#Abrir archivo
ruta= str(pathlib.Path().absolute())+"/14-Sistemas-Archivos/fichero_texto.txt"
print(ruta)
archivo_lectura = open(ruta, "r")

#Leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

#Leer contenido y guardar en la lista
lista= archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    #lista_frase= frase.split("\n")
    #print(lista_frase)
    print("- "+ frase.center(10))
    
#Copiar
"""
ruta_origen= str(pathlib.Path().absolute())+"/14-Sistemas-Archivos/fichero_texto.txt"
ruta_nueva=str(pathlib.Path().absolute())+"/14-Sistemas-Archivos/fichero_copiado.txt"
ruta_alternativa= str(pathlib.Path().absolute())+"/07-Ejercicios/fichero_copiado88.txt" 
shutil.copyfile(ruta_origen, ruta_nueva)
"""
#Mover
"""
ruta_origen=str(pathlib.Path().absolute())+"/14-Sistemas-Archivos/fichero_copiado.txt"
ruta_nueva=str(pathlib.Path().absolute())+"/14-Sistemas-Archivos/fichero_copiado_NUEVO.txt"

shutil.move(ruta_origen, ruta_nueva)
"""
#Eliminar
import os
"""
ruta_eliminar= str(pathlib.Path().absolute())+"/14-Sistemas-Archivos/fichero_copiado_NUEVO.txt"
os.remove(ruta_eliminar)
"""
#Comprobar si existen
import os.path

#print(os.path.abspath("/"))
ruta_comprobar= str(pathlib.Path().absolute())+"/14-Sistemas-Archivos/fichero_texto.txt"
print(ruta_comprobar)

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")