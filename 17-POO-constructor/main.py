from coche import Coche
#Usando el constructor para los detalles
carro_1 = Coche("Amarillo", "Renault", "Clio", 150, 200, 5)
carro_2 = Coche("Verde", "Seat", "Panda", 240, 200, 5)
carro_3 = Coche("Amarillo", "Renault", "Clio", 100, 180, 5)
carro_4 = Coche("Amarillo", "Renault", "Clio", 350, 400, 5)

#Usando getInfo
print(carro_1.getInfo())
print(carro_2.getInfo())
print(carro_3.getInfo())
print(carro_4.getInfo())

#Detectar tipado
carro_3="Aleatorio"
if type(carro_3)== Coche:
    print("Es un objeto correcto.")
else:
    print("No es un objeto.")

#Visibilidad
#print(carro_1.soy_publico)
#print(carro_1._soy_privado)
print(carro_1.getPublico())
print(carro_1.getPrivado())