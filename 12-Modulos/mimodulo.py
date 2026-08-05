def holaMundo(nombre):
    return f"Hola como estás, {nombre}!"

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