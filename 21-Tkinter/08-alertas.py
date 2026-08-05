from tkinter import *
from tkinter import messagebox as MessageBox

ventana=Tk()
ventana.config(bd=70)

def sacarAlerta():
    #En el messagebox la primera palabra sera el titulo, mientras que la segunda será el mensaje
    MessageBox.showerror("Alerta", "Hola soy Christian Freire")

Button(ventana,text="¡¡¡Mostrar alerta!!!",command=sacarAlerta).pack()

def salir(nombre):
    resultado=MessageBox.askquestion("Salir", "¿Coninuar ejecutando la aplicación?")
    
    if resultado != "yes":
        MessageBox.showinfo("¡Chao!",f"Adios, {nombre}")
        ventana.destroy()

Button(ventana,text="Salir",command = lambda:salir("Christian Freire")).pack()
    

ventana.mainloop()