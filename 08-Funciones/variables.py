"""
Variable locales: Se definen dentro de la función y no 
se pueden usar fuera de ella, solo están disponibles dentro. 
A no ser que hagamos un return.

Variables globales Son las que se declaran fuera de una función y estan disponibles dentro y fuera de ellas
"""
#Variable global
frase="Ni los genios son tan genios ni los mediocres tan mediocres"

print(frase)

def holaMundo():
    #Variable local
    frase="Hola Mundo"
    print("Dentro de la función: ")
    print(frase)
    
    year=2026
    print(year)
    
    global website
    website="www.freirechristian.com"
    print(website)
    
    
    return "Dato envuelto" + str(year)

holaMundo()
print("Fuera de la función: ")
print(website)