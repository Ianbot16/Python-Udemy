"""
Ejercicio 4: Crear un script que tenga 4 variables, una lista, un string, 
un entero y un booleano y qque imprima un mensaje 
según el tipo de dato de cada variable. Usar funciones.
"""

def traducirTipo(tipo):
    result= None
    if tipo == list:
        result="lista"
    elif tipo == str:
        result="cadena de texto"
    elif tipo == int:
        result="entero"
    elif tipo == bool:
        result="booleano"
    return result

def comprobarTipado(dato, tipo):
    test= isinstance(dato, tipo)
    result=" "
    
    if test:
        print(f"Ese dato es del tipo {traducirTipo(tipo)}")
    else:
        result="El tipo de dato no coincide con el tipo esperado"
    return result



mi_lista=["Hola mundo",77]
titulo="Master en Python"
numero=42
verdadero=True

print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))