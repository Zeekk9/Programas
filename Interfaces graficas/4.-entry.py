from tkinter import *

# configuracion de la raiz
root = Tk()
# Sticky lo alinea a izquierda o derecha, esteo o este
# Grid crea una rejilla en este caso de 2x2
#Padx,Pay agrega un margen
#Justify justifica el texto escrito
#State desactiva o modifica el modificar texto, disable, normal, enabled
label = Label(root, text="Nombre mu largo")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right",state="disabled")

label2 = Label(root, text="Apellidos")
label2.grid(row=1, column=0, sticky="e", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="center",show="*")


# Finalmente bucle de la aplicacion
root.mainloop()
