"""
# FOR
for variable in elemento_iterable (lista, rango, etc):
    bloque de instrucciones
    
"""
contador=0
resultado=0

for contador in range(0,10):
    print("Voy por el ", str(contador))
    
    #resultado=resultado+contador
    resultado+=contador
    
print("El resultado es: ", str(resultado))

#Ejemplo tablas de multiplicar
print("\n#########EJEMPLO BUCLE IF########")
numero_usuario=int(input("¿De qué número quieres la tabla de multiplicar?: "))

if numero_usuario>=1:
    print(f"#### La tabla de multiplicar del {numero_usuario} ####")
    for numero_tabla in range(1,13):
        if numero_usuario==45:
            print("No se pueden mostrar números prohibidos")
            break
        print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
    print("Tabla finalizada")
#Este else pertenece al if, por lo que se ejecutará si el número ingresado es menor a 1
else:
    print("Use un número mayor a 0")
    
#Segunda forma de mostrar la tabla de multiplicar
#Ejemplo tablas de multiplicar
print("\n#########EJEMPLO BUCLE FOR########")
numero_usuario=int(input("¿De qué número quieres la tabla de multiplicar?: "))
#Este bucle if es para evitar que el usuario ingrese un número menor a 1, 
#ya que no tendría sentido mostrar la tabla de multiplicar de números negativos o del 0

if numero_usuario<1:#Si revisa si el número es menor a 1
    numero_usuario=1#Sí es así, se le asigna el valor de 1 para que el programa pueda continuar y mostrar la tabla de multiplicar del 1
#Hecho esto, el programa continúa normalmente, mostrando la tabla de multiplicar del número ingresado por el usuario, 
#o del 1 si el número ingresado era menor a 1    
print(f"#### La tabla de multiplicar del {numero_usuario} ####")

#Aquí se crea el bucle for para mostrar la tabla de multiplicar del número ingresado por el usuario, 
#o del 1 si el número ingresado era menor a 1
for numero_tabla in range(1,13):
    if numero_usuario==45:
        print("No se pueden mostrar números prohibidos")
        break
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
#Este else pertenece al for, no al if, 
#por lo que se ejecutará si el for se ejecuta completamente sin interrupciones (break)
else:
    print("Tabla finalizada")