"""
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En formato clave-valor.
Es parecido a un array asociativo o a un objeto JSON.
"""

persona = {
    "nombre":"Christian",
    "apellido":"Freire",
    "web":"christianfreire.com"
}

print(type(persona))
print(persona)
print(persona["apellido"])

#Lista de diccionarios
print("\n*****Lista de diccionarios*****")
contactos = [
    {
        "nombre":"Antonio",
        "email":"antonio@correo.com"
    },
    {
        "nombre":"Luis",
        "email":"luis@correo.com"
    },
    {
        "nombre":"Salvador",
        "email":"salvador@correo.com"
    },
    {
        "nombre":"Maria",
        "email":"maria@correo.com"
    }
]

contactos[0]["nombre"]="Antoñito"
print(contactos[0]["nombre"])

print("\n*****Lista de contactos*****")
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("--------------------------")
    