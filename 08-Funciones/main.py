"""
FUNCIONES:
Una función es un conjunto de instrucciones agrupadas bajo 
un nombre concreto que pueden reutilizarse invocando a 
la función tantas veces como sea necesario.

def nombre_funcion(parametros):
    #Bloque / Conjunto de instrucciones
    
nombre_funcion(mi_parametro) #Llamada a la función
nombre_funcion(mi_parametro)

"""

#Ejemplo 1
print("\n#### Ejemplo 1 ####")

#Definir la función
def muestraNombre():
    print("Christian")
    print("Victoria")
    print("Sebastian")
    print("Arturo")
    print("Anastacia")
    print("Sofia")
    print("\n")
    
#Llamar a la función
muestraNombre()
muestraNombre()
muestraNombre()

#Ejemplo 2: Parametros en las funciones
print("\n#### Ejemplo 2 ####")

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    if edad >= 18:
        print("Y eres mayor de edad")
    else:
        print("Y eres menor de edad")

#Se pide el nombre al usuario y con esto se llama a la función
#nombre = input("Introduce tu nombre: ")
#edad = int(input("Introduce tu edad: "))
mostrarTuNombre("Christian", 23)#nombre, edad

#Ejemplo 3
print("\n#### Ejemplo 3 ####")

def tablaMultiplicar(numero):
    print(f"Tabla de multiplicar del {numero}")
    
    for contador in range(1,13):
        operacion = numero * contador
        print(f"{numero} x {contador} = {operacion}")
    print("\n")

tablaMultiplicar(3)
tablaMultiplicar(6)
tablaMultiplicar(9)
tablaMultiplicar(12)

#Ejemplo 3.1
print("--------------------------------")
for numero_tabla in range(1,13):
    tablaMultiplicar(numero_tabla)
    
#Ejemplo 4
print("\n#### Ejemplo 4 ####")

#Parametros opcionales
def getEmpleado(nombre,ced=None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    
    if ced != None:
        print(f"Cedula: {ced}")
    
getEmpleado("Christian Freire", "0954343208")    

#Ejemplo 5: Parametros opcionales y return o devolver datos
print("\n#### Ejemplo 5 ####")
def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    
    return saludo

print(saludame("Christian"))

#Ejemplo 6
print("\n#### Ejemplo 6 ####")

def calculadora(numero1, numero2, basicas=False):
    
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2
    
    cadena = ""
    
    if basicas != False:
        cadena += "Suma : " + str(suma) + "\n"
        cadena += "Resta : " + str(resta) + "\n"
        cadena += "Multiplicacion : " + str(multi) + "\n"
        cadena += "Division : " + str(division) + "\n"
    
    return cadena

print(calculadora(10, 5,True))

#Ejemplo 7
print("\n#### Ejemplo 7 ####")

def getNombre(nombre):
    texto=f"El nombre es: {nombre}"
    return texto


def getApellidos(apellidos):
    texto=f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Christian", "Freire"))

#Ejemplo 8: Funciones lambda
print("\n#### Ejemplo 8 ####")
dime_el_año = lambda año: f"El año es: {año * 50}"
print(dime_el_año(2026))