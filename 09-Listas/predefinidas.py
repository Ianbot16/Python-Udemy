bandas=["Metallica", "Megadeth", "Queen", "Guns n Roses"]
numeros=[1,2,5,6,3,4]

#Ordenar
print(numeros)
numeros.sort()
print(numeros)

#Añadir elementos a la lista
bandas.append("Enanitos Verdes")
bandas.insert(1,"Aerosmith")
print(bandas)

#Eliminar elementos de la lista
bandas.pop(1)
bandas.remove("Enanitos Verdes")
print(bandas)

#Dar la vuelta a la lista
print(numeros)
numeros.reverse()
print(numeros)

#Buscar dentro de la lista
print("Metallica" in bandas)

#Contar elementos de la lista
print(bandas)
print(len(bandas))

#Cuantas veces aparece un elemento en la lista
print(numeros)
numeros.append(6)
print(numeros.count(6))

#Conseguir el indice de un elemento
print(bandas)
print(bandas.index("Queen"))