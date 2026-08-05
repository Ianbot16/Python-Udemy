"""
Ejercicio 1: Hacer un programa que tenga una lista de 8 números enteros y haga lo siguiente:
-Recorrer la lista y mostrarla (hecho)
-Hacer una función que recorra listas de números y devuelva un string(hecho)
-Ordenarla y mostrarla (hecho)
-Mostrar su longitud (hecho)
-Buscar algún elemento (que el usuario pida por teclado)
"""


#Crear la lista
numeros=[13,64,52,73,21,7,91,63]

#Crear la función que recorra la lista y devuelva un string
def mostrarLista(lista):
    resultado=""
    
    for elemento in lista:
        resultado+="Elemento: "+str(elemento)
        resultado+="\n"
    return resultado

#Recorre y mostrar la lista
print("#####Recorrer y mostrar la lista#####")
"""
for numero in numeros:
    print(numero)
"""
print(mostrarLista(numeros))

#Ordenar y mostrar
print("#####Ordenar y mostrar#####")
numeros.sort()
print(mostrarLista(numeros))

print("#####Mostrar longitud#####")
print(len(numeros))

#Busqueda en la lista
try:
    print("#####Busqueda en la lista#####")
    busqueda=int(input("Ingrese el número a buscar: "))

    comprobar=isinstance(busqueda,int)

    while not comprobar or busqueda<=0:
        busqueda=int(input("Ingrese un número: "))

    else:
        print("Has ingresado el número: ", busqueda)

    print(f"#####Buscar el número {busqueda} en la lista#####")

    search=numeros.index(busqueda)
    print(f"El número existe en la lista, es el índice: {search}")
except:
    print("El número no existe en la lista.")