"""
Ejercicio 5: Hacer un programa que muestre los números entre dos números que diga el usuario.
"""

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))

if numero_1 < numero_2:
    for contador in range(numero_1, (numero_2+1)):
        print(contador)
else:
    print("El primer número debe ser menor al segundo número")