"""
Ejercicio 8: ¿Cuanto es el X por ciento de X número? De 20 % de 150, por ejemplo.
"""

numero = int(input("Ingrese el número: "))
porcentaje = int(input(f"¿Qué porcentaje desea calcular de {numero}?: "))
operacion = (numero * porcentaje) / 100
if porcentaje <= 100:
    print(f"El {porcentaje}% de {numero} es: {operacion}")
else:    
    print("El porcentaje debe ser menor a 100%")
