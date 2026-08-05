"""
Ejercicio 10: El programa tiene que pedir la nota de 15 alumnosy sacar por pantalla 
y sacar por pantalla cuantos han aprobado y cuantos han suspendido.
"""

contador = 1
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("¿Cuantos alumnos tiene?: "))

while contador <= numero_alumnos:
    nota=int(input(f"¿Qué nota quieres ponerle al \"alumno N° {contador}?: "))
    
    if nota >= 7 and nota <= 10:
        aprobados += 1
    else:
        suspendidos += 1
    
    contador += 1
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos suspendidos: {suspendidos}")