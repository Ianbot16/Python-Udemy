"""
Modulos: son funcionlidades ya hechas para reutiliar.

En python hay muchos modulos, que los puedes consultar aquí: 
https://docs.python.org/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje, 
modulos en internet, y tambien podemos crear nuestros propios modulos.

"""

#Importar el modulo propio
#import mimodulo
#from mimodulo import holaMundo, calculadora
from mimodulo import *

#print(mimodulo.holaMundo("Christian Freire"))
#print(mimodulo.calculadora(3, 5, True))

print(holaMundo("Christian Freire"))
print(calculadora(3, 5, True))

# Modulo fechas
import datetime
#Muestra la fecha actual
print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)
print(fecha_completa.hour)

#fecha_personaliada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S") 
fecha_personaliada = fecha_completa.strftime("%d/%m/%Y")
hora_personalizada = fecha_completa.strftime("%H:%M:%S")
print(fecha_personaliada)
print(hora_personalizada)
print("Mi fecha personalizada es: " + fecha_personaliada)
print("Mi hora personalizada es: " + hora_personalizada)
print(datetime.datetime.now().timestamp())

#Modulo matematico
import math

print("Raíz cuadrada de 10: ", math.sqrt(10))
print("Número pi: ", float(math.pi))
print("Redondear: ", math.ceil(6.56798))
print("Redondear a la baja: ", math.floor(6.56798))

#Modulo random
import random
print("Número aleatorio entre 15 y 67: ", random.randint(15, 67))