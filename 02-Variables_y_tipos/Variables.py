#Una variable es un espacio en la memoria de la computadora que se utiliza para almacenar datos.
#En Python, no es necesario declarar el tipo de variable, 
#ya que el lenguaje es dinámico y se asigna automáticamente el tipo de dato según el valor que se le asigne.
texto = "Máster en Python"
texto_2 = "Con Christian Freire"
numero = 42
decimal = 3.14
print(texto)
print(texto_2)
print(numero)
print(decimal)
print("-----------------------------------")
#Sustituimos los valores de las variables por otros nuevos
numero = 100
decimal = 2.718
print(numero)
print(decimal)
print("-----------------------------------")

#Concatenación de variables
nombre = "Christian"
apellido = "Freire"
web="www.freirechristian16.com"
print(nombre + " " + apellido +" - " + web)
print(f"{nombre} {apellido} - {web}")
print("{} {} - {}".format(nombre, apellido, web))
print("Hola me llamo {} {} y mi sitio web es {}".format(nombre, apellido, web))
print(nombre, apellido, web)
