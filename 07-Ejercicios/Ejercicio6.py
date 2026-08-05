"""
Ejercicio 6: Mostrar las tablas de multiplicar del 1 al 12.
Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 12.
"""

for cabecera in range(1,13):
    print("#####################")
    print(f"####Tabla del {cabecera}####")
    print("#####################")
    
    for numero in range(1,13):
        print(f"{numero} x {cabecera} = {numero * cabecera}")
        
    print("\n")