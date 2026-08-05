"""
Ejercicio 3: Programa que compruebe si una variable está vacía y si está vacia, 
rellenarla con texto en minusculas y mostrarlo en mayusculas.
"""

texto =" "

if len(texto.strip()) <= 0:
    #mostrar el texto
    texto ="Hola, soy un texto en minusculas"
    print(texto.upper())
else:
    print(f"La variable tiene contenido {texto}")