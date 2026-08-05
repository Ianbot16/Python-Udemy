#Capturar excepciones y manejar errores en código susceptible a fallos o errores.
"""
nombre=input("¿Cuál es tu nombre?: ")

try:
    if len(nombre) > 1 :
        nombre_usuario=f"Tu nombre es {nombre}"  
        
    print(nombre_usuario)
    
except:
    print("Ha ocurrido un error.")

else:
    print("El código se ha ejecutado correctamente.")
finally:
    print("Fin del programa.")
"""

#Multiple excepciones
"""
try:
    numero=int(input("Ingrese un número para elevarlo al cuadrado: "))
    print("El resultado es: "+str(numero**2))
except TypeError:
    print("Debes convertir tus cadenas en el código.")
#except ValueError:
#    print("Introduce un número válido.")
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error:", type(e).__name__)
"""

#Excepciones personalizadas
try:
    nombre=input("Introduce tu nombre: ")
    edad=int(input("Introduce tu edad: "))

    if edad < 5 and edad > 120:
        raise ValueError("La edad introducida no es válida.")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo.")
    else:
        print(f"Bienvenido/a al Máster en Python, {nombre}.")
except ValueError:
    print("Introduce los datos correctamente.")
except Exception as e:
    print("Ha ocurrido un error:", type(e).__name__)