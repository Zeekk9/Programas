from tkinter import *

# Configuracion de la raiz
root = Tk()

#Imagenes en lavels

imagen = PhotoImage(file="tenor.gif")
Label(root,image=imagen,bd=0).pack(side="left")


root.mainloop()
