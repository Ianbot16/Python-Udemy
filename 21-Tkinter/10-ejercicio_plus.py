"""
CALCULADORA:
- Dos campos de texto
- 4 botones para las operaciones
-Mostrar el resultado de una alerta
"""

from tkinter import *
from tkinter import messagebox 

class Calculadora:
    
    def __init__(self, alertas):
        self.n1=StringVar()
        self.n2=StringVar()
        self.R=StringVar()
        self.alertas=alertas

    def cFloat(self,numero):
        try:
            result=float(numero)
        except:
            result=0
            messagebox.showerror("Error","Introduce bien los datos")
            
        return result

    def sumar(self):
            self.R.set(self.cFloat(self.n1.get())+self.cFloat(self.n2.get()))
            self.mostrarResultado()
        

    def restar(self):
        self.R.set(self.cFloat(self.n1.get())-self.cFloat(self.n2.get()))
        self.mostrarResultado() 
        

    def multiplicar(self):
            self.R.set(self.cFloat(self.n1.get())*self.cFloat(self.n2.get()))
            self.mostrarResultado()
        

    def dividir(self):
            self.R.set(self.cFloat(self.n1.get())/self.cFloat(self.n2.get()))
            self.mostrarResultado()
        
        
    def mostrarResultado(self):
        self.alertas.showinfo("Resultado",f"El resultado de la operación es: {self.R.get()}")
        self.n1.set("")
        self.n2.set("")

ventana=Tk()
ventana.title("Ejercicio completo con Tkinter | Christian Freire")
ventana.geometry("400x400")
ventana.config(bd=25)

calculadora=Calculadora(messagebox)

marco=Frame(ventana, width=300, height=200)
marco.config(
    bd=5,
    padx=15,
    pady=15,
    relief=SOLID,
    
)
marco.pack(side=TOP,anchor=CENTER)
marco.pack_propagate(False)

Label(marco,text="Primer número: ").pack()
Entry(marco,textvariable=calculadora.n1,justify="center").pack()

Label(marco,text="Segundo número: ").pack()
Entry(marco,textvariable=calculadora.n2,justify="center").pack()

Label(marco,text="").pack()

Button(marco, text="Sumar",command=calculadora.sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Restar",command=calculadora.restar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Multiplicar",command=calculadora.multiplicar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Dividir",command=calculadora.dividir).pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()