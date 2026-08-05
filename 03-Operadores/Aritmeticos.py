#Operadores aritméticos
numero_1= 77
numero_2= 33
#suma= numero_1 + numero_2
resta= numero_1 - numero_2
multiplicacion= numero_1 * numero_2
division= numero_1 / numero_2

print("*************************Calculadora************************")
print(f"La suma es: {numero_1+numero_2}")
print(f"La resta es: {resta}")
print(f"La multiplicación es: {multiplicacion}")
print (f"La división es: {division:.2f}") #El .2f es para mostrar solo 2 decimales
print(f"La división es: {division}")
division_redondeada = round(division, 2) #El round es para redondear el resultado a 2 decimales
print(f"La división redondeada es: {division_redondeada}")
print(f"La división entera es: {numero_1 // numero_2}") #La división entera muestra el resultado sin decimales
print(f"El módulo es: {numero_1 % numero_2}") #El módulo muestra el resto de la división
print(f"La potencia es: {numero_1 ** numero_2}") #La potencia muestra el resultado de elevar un número a otro
