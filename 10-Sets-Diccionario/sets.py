"""
SET es un tipo de dato, para tener una colección de valores, pero no tiene ni indices ni orden.
"""

personas={
    "Christian",
    "Maria",
    "Pedro"
}

personas.add("Ana")
personas.remove("Pedro")

print(type(personas))
print (personas)