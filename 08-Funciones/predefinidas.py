nombre="Christian Freire"

#funciones generales
print(type(nombre))

#Detectar el tipado
comprobar= isinstance(nombre, str)
if comprobar:
    print("La variable es un string")

else:
    print("La variable no es un string")
    
if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

#Limpiar espacios
frase="   mi contenido   "
print(frase)
print(frase.strip())

#Eliminar variables
year=2026
print(year)
del year

#Comprobar variable vacía
texto="  ff  "
if len(texto)<=0:
    print("La variable está vacía")
else:
    print("La variable tiene contenido: ", len(texto))

#Encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida"))

#Reemplazar palabras en un string
nueva_frase=frase.replace("vida", "moto")
print(nueva_frase)

#Mayusculas y minusculas
print (nombre)
print(nombre.upper())
print(nombre.lower())