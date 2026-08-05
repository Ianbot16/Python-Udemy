"""
Ejercicio 9: Hacer un programa que pida números al usuario indefinidamente hasta meter el número 111.
"""

contador=1
while contador <= 100:
    n=int(input("Ingrese un número: "))
    
    if n == 111:
        print("¡Has ingresado el número 111! El programa se detendrá.")
        break
    else:
        print(f"Has ingresado el número {n}.")

