from tkinter import *

ventana=Tk()
ventana.geometry("750x500")

texto=Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="#000000",
    padx=50,
    pady=20,
    font=("Arial",30))
texto.pack()

texto=Label(ventana, text="Soy Christian Freire")
texto.config(
    height=3,
    bg="orange",
    font=("Arial",18),
    padx=10,
    pady=10,
    cursor="spider"
)
texto.pack(anchor=SE)

def pruebas(nombre, apellido, pais):
    return f"Hola {nombre} {apellido}, veo que eres de {pais}"
    

texto=Label(ventana, text=pruebas(apellido="Freire",pais="Ecuador",nombre="Christan"))
texto.config(
    height=3,
    bg="green",
    font=("Arial",18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(anchor=NW)

ventana.mainloop()