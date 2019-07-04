from tkinter import *

# Configuracion de la raiz
root = Tk()
""
# Varaiables dinamicas
texto = StringVar()
texto.set('Un nuevo texto')
'''
#Configuracion de un marco
frame = Frame(root, width=480, height=320)
frame.pack()
#En lugar de un frame puede utilizarse la raiz para poner el label afuera del marco

#Se pone frame para que este dentro del marco junto con pack
label = Label(frame, text="hola mundo")
#label.pack()
#se utiliza place para poner el texto en algun lugar especifico
label.place(x=100,y=100) 
#Abajo del todo'''

# Otra forma de gregar etiquetas
# Se respeta el orden de enpaquetacion, la primera aparece primero etc
Label(root, text='Hola mundo').pack(anchor="nw")
label = Label(root, text='Otra etiqueta')
Label(root, text='Kaka').pack(anchor='se')

label.pack(anchor='center')
# bg=backgroud,fg=fontground
label.config(bg="green", fg="blue", font=("Verdana", 24))
label.config(textvariable=texto)

root.mainloop()
