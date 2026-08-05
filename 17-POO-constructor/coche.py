#Programación Orienada a objetos (POO o OPP)
#Definir una clase (molde para crear más objetos de ese tipo (Coche) con caracteristicas similares)
class Coche:
    #Atributos o propiedades (variables)
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    soy_publico = "Hola, soy un atributo publico"
    _soy_privado = "Hola, soy un atributo privado"
    
#Constructor
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

#Metodos, son acciones que hace el objeto (coche) (funciones)
    def getPublico(self):
        return self.soy_publico
    
    def getPrivado(self):
        return self._soy_privado
    
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo
    
    def setMarca(self,marca):
        self.marca = marca
        
    def getMarca(self):
        return self.marca
        
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad
    
    def getInfo(self):
        info = "\n -----Información del carro-----"
        info += "\n Color: "+ self.getColor()
        info += "\n Marca: "+ self.getMarca()
        info += "\n Modelo: "+ self.getModelo()
        info += "\n Velocidad: "+ str(self.getVelocidad())
        
        return info

#fin definicion clase
