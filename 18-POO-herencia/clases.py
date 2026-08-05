#Herencia: Es la posibilidad de compartir atributos y métodos entre clases. Y que diferentes clases hereden de otras.
class Persona:
    """
    nombre 
    apellido 
    altura
    edad
    """
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getAltura(self):
        return self.altura 
    
    def getEdad(self):
        return self.edad
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setAltura(self, altura):
        self.altura = altura 
    
    def setEdad(self, edad):
        self.edad = edad
    
    def hablar(self):
        return "Estoy hablando"
    
    def caminar(self):
        return "Estoy caminando"
    
    def dormir(self):
        return "Estoy durmiendo"
    

class Informatico(Persona):
    """
    lenguajes
    experiencia
    """
    
    def __init__(self):
        self.lenguajes = "C++, Python, Java, HTML5"
        self.experiencia = 5
        
    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"
    
    def repararPC(self):
        return "Estoy reparando tu ordenando"

class TecnicoRedes(Informatico):
    
    def __init__(self):
        #Con esto podemos usar los datos __init__ de la clase padre
        super().__init__()
        self.auditarRedes = "Experto"
        self.experienciaRedes = 15
        
    def auditoria(self):
        return "Estoy auditando una red"
    
    
    
    