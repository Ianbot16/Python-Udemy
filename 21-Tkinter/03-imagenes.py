from tkinter import *
from PIL import Image,ImageTk

ventana=Tk()
ventana.geometry("700x500")

Label(ventana, text="Hola, soy Christian Freire").pack(anchor=W)

imagen = Image.open("./21-Tkinter/imagenes/lobo_gris.jpg")
render=ImageTk.PhotoImage(imagen)

Label(ventana,image=render).pack(anchor=E)
ventana.mainloop()