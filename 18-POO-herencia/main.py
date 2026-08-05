import clases

persona = clases.Persona()
persona.setNombre("Christian")
persona.setApellido("Freire")
persona.setAltura(1.65)
persona.setEdad(23)

print(f"La persona es: {persona.getNombre()} {persona.getApellido()}.")
print(f"Tiene una altura de: {persona.getAltura()} m.")
print(f"Tiene la edad de: {persona.getEdad()} años.")
print(persona.hablar())
print("-------------------------------------")

informatico=clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellido("Robles")

print(f"El informatico es: {persona.getNombre()} {persona.getApellido()}.")
#print(informatico.lenguajes)
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)

print("--------------------------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Martín")
tecnico.setApellido("Castillo")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getApellido(), tecnico.getLenguajes())