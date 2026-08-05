def mi_funcion(nombre):
    return "Hola como estas " + nombre
    
def mi_segunda_funcion(apellido):
    return "Hola, como estas tú " + apellido

nombre="Christian"
apellido="Freire"

print("Hola mundo")
print(f"Bienvenido {nombre} {apellido}")

print(mi_funcion(nombre))
print(mi_segunda_funcion(apellido))
