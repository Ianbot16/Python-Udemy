""""
#Condicional If
Si se cumple esta condición:
  Ejecutar grupo de instrucciones
Si no:
  Se ejecuta otro grupo de instrucciones

if condición:
    Instrucciones a ejecutar si se cumple la condición
else:
    Instrucciones a ejecutar si no se cumple la condición 
    
    
    
#Operadores de comparación
== Igual a
!= Distinto a
> Mayor que
< Menor que
>= Mayor o igual que
<= Menor o igual que

#Operadores lógicos
and (y) -> Todas las condiciones deben cumplirse
or (o) -> Al menos una de las condiciones debe cumplirse
! negación -> Niega la condición
not (no) -> Niega la condición
"""
#Ejemplo 1
print("\n***********Ejemplo 1***********")
color = "rojo"
#color = input("Adivina cual es mi color favorito: ")
if color == "rojo" or color == "Rojo":
    print("Enhorabuena")
    print("El color es rojo")
else:
    print("Color incorrecto")

#Ejemplo 2
print("\n***********Ejemplo 2***********")
year=2020
#year = int(input("¿En que año estamos?: "))
if year >= 2020:
    print("Estamos de 2020 para adelante")
else:   
    print("Estamos antes de 2020")

#Ejemplo 3
print("\n***********Ejemplo 3***********")
nombre = "Christian Freire"
ciudad = "Durán"
continente = "América"
edad= 22
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    
    if continente != "América":
        print(f"{nombre} no es de América")
    else:
        print(f"{nombre} es de América")
else:
    print(f"{nombre} no es mayor de edad")

#Ejemplo 4
print("\n***********Ejemplo 4***********")
dia=int(input("Introduce el numero del dia de la semana (1-5): "))

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es fin de semana")

#Ejemplo 5
print("\n***********Ejemplo 5***********")
edad_minima = 18
edad_maxima = 65
edad_oficial = 17
if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print("Está en edad de trabajar")
else:
    print("No está en edad de trabajar")

#Ejemplo 6
print("\n***********Ejemplo 6***********")
pais = "Alemania"

if pais == "México" or pais == "España" or pais == "Colombia" or pais == "Ecuador" or pais == "Perú":
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} no es un país de habla hispana")

#Ejemplo 7
print("\n***********Ejemplo 7***********")
pais = "Ecuador"

if not (pais == "México" or pais == "España" or pais == "Colombia" or pais == "Ecuador" or pais == "Perú"):
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} no es un país de habla hispana")

#Ejemplo 8
print("\n***********Ejemplo 8***********")
pais = "Colombia"
if pais != "México" and pais != "España" and pais != "Colombia" and pais != "Ecuador" and pais != "Perú":
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} no es un país de habla hispana")