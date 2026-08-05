"""
Ejercicio 3: Escribir un programa que muestre los cuadrados (Número multiplicado por sí mismo) de los primeros 60 números naturales.
Resolverlo con for y con while.
"""

#While
contador = 0
while contador <= 60:
    
    cuadrado = contador * contador
    print(f"El cuadrado de {contador} es {cuadrado}")
    
    contador += 1
print("-------------------------------")    
#For
for numero in range(61):
    
    cuadrado = numero * numero
    print(f"El cuadrado de {numero} es {cuadrado}")