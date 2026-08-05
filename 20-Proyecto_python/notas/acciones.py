import notas.nota as modelo

class Acciones:
    
    def crear(self, usuario):
        print(f"Ok {usuario[1]}, vamos a crear una nueva nota")
        
        titulo=input("Ingrese el titulo de su nota: ")
        descripcion= input("Ingrese el contenido de su nota: ")
        
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar=nota.guardar()
        
        if guardar[0]>=1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")
    
    def mostrar(self,usuario):
        print(f"\nBien {usuario[1]}, aquí tienes tus notas: ")
        
        nota = modelo.Nota(usuario[0])
        notas=nota.listar()
        
        for nota in notas:
            print("*****************************************")
            print(nota[2])
            print(nota[3])
            print("*****************************************")
    
    def borrar(self, usuario):
        print(f"\nOk {usuario[1]}, vamos a borrar notas. ")
        
        titulo=input("Ingrese el titulo de la nota a eliminar: ")
        
        nota=modelo.Nota(usuario[0], titulo)
        eliminar=nota.eliminar()
        
        if eliminar[0]>=1:
            print(f"Hemos borrado la nota: {nota.titulo}")
            
        else:
            print("No se ha borrado la nota, prueba luego...")
            