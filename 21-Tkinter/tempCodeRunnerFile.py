"""
CALCULADORA:
- Dos campos de texto
- 4 botones para las operaciones
-Mostrar el resultado de una alerta
"""

from tkinter import *
from tkinter import messagebox 

ventana=Tk()
ventana.title("Ejercicio completo con Tkinter | Christian Freire")
ventana.geometry("400x400")
ventana.config(bd=25)

def cFloat(numero):
    try:
        result=float(numero)
    except:
        result=0
        messagebox.showerror("Error","Introduce bien los datos")
        
    return result

def sumar():
        R.set(cFloat(n1.get())+cFloat(n2.get()))
        mostrarResultado()
    

def restar():
       R.set(cFloat(n1.get())-cFloat(n2.get()))
       mostrarResultado() 
       

def multiplicar():
        R.set(cFloat(n1.get())*cFloat(n2.get()))
        mostrarResultado()
    

def dividir():
        R.set(cFloat(n1.get())/cFloat(n2.get()))
        mostrarResultado()
    
    
def mostrarResultado():
    messagebox.showinfo("Resultado",f"El resultado de la operación es: {R.get()}")
    n1.set("")
    n2.set("")

n1=StringVar()
n2=StringVar()
R=StringVar()

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
Entry(marco,textvariable=n1,justify="center").pack()

Label(marco,text="Segundo número: ").pack()
Entry(marco,textvariable=n2,justify="center").pack()

Label(marco,text="").pack()

Button(marco, text="Sumar",command=sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Restar",command=restar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Multiplicar",command=multiplicar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Dividir",command=dividir).pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()