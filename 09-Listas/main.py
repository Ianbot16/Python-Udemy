"""
LISTAS(arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico nombre.
Para acceder a esos valores, se utiliza un indice numerico.
"""

pelicula="El señor de los anillos"

#Definir la lista
peliculas=["El señor de los anillos", "Batman", "Spiderman"]
bandas=list(("Metallica", "Megadeth", "Queen", "Guns n Roses"))
years=list(range(2000,2026))
variada=["Christian",30,4.5,True,"Texto"] 
"""
print(peliculas)
print(bandas)
print(years)
print(variada)
"""

#Indices
pelicula="otra cosa"
peliculas[1]="Gran Torino"
peliculas[2]="El Hobbit"
print(peliculas)
print(peliculas[1])
print(peliculas[-2])
print(bandas[1:4])
print(bandas[2:])

#Añadir elementos a la lista
bandas.append("Enanitos Verdes")
bandas.append("Aerosmith")
print(bandas)

#Recorrer una lista
print("\n*****Listado de bandas*****")
for banda in bandas:
    print(f"{bandas.index(banda)}. {banda}")

"""
nueva_pelicula=""
while nueva_pelicula != "parar":
    nueva_pelicula=input("Introduce una nueva pelicula o 'parar' para finalizar: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)
"""
    
print("\n*****Listado de peliculas*****")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")
    
#Listas multidimensionales
print("\n *****Listado de contactos*****")
contactos=[
    [
        "Christian",
        "christian@email.com"
    ],
    [
        "Luis",
        "luis@email.com"
    ],
    [
        "Maria",
        "maria@email.com"
    ],
    [
        "Antonio",
        "antonio@email.com"
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")

#print(contactos)
#print(contactos[1][1])