"""
Ejercicio 2: Escribir un programa que añada valores a una lista 
mientras que su longitud sea menor a 50 y luego mostrar la lista.
Plus: Usar while y for
"""
#Forma del while
print("\n*****Lista con el bucle while*****")
coleccion_while=[]
x=0

while x<50:
    coleccion_while.append(f"Elemento del bucle - {x}")
    print ("Mostrando el: "+ coleccion_while[x])
    x+=1

print(coleccion_while[25])   

#Forma del for
print("\n*****Lista con el bucle for*****")
coleccion_lista=[]

for contador in range(0,50):
    coleccion_lista.append(f"Elemento de la lista - {contador}")
    print ("Mostrando el: "+ coleccion_lista[contador])
print (coleccion_lista[25])
