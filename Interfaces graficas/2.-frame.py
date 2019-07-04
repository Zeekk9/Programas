from tkinter import *

root = Tk()

#Titulo
root.title("Hola mundo")
#Expandir o contrar, 0,1, solo horizontal, 1,0 solo vertical
root.resizable(1, 1)
root.iconbitmap('Martz90-Circle-Plex.ico')

#Crear marco,root=raiz
frame = Frame(root, width=480, height=320)
#Empaquecar, side=left,right,bottom,
#Anchor=w,e,o, este oeste, norte, sur
#frame.pack(side="bottom", anchor="w")
#fill=X o Y,expand=1 o 'both',expand=1
frame.pack(fill='both',expand=1)
#Configuracion
frame.config(cursor="pirate")
#Color de fondo
frame.config(bg="lightblue")
#Tamaño del relieve
frame.config(bd=25)
#Relieve
frame.config(relief="sunken")

#Se aplica la configuracion a la raiz
root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")



#Abajo del todo
root.mainloop()
