"""
Ejercicio 7: Hacer un programa que muestre todos los números impares entre dos números que decida el usuario.
"""

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

if n1 < n2:
    for x in range(n1, (n2+1)):
        if x % 2 == 0:
            print(f"{x} es par")
        else:
            print(f"{x} es impar")

else: 
    print("El primer número debe ser menor al segundo número")