from distutils.command.clean import clean
from inspect import CO_ASYNC_GENERATOR
from tkinter import * 

root = Tk() 
pantalla = StringVar() 
pantalla2 = StringVar()
datos = StringVar()


def getdatos():
    nombre = pantalla.get()
    apellido = pantalla2.get()
    datos.set(nombre+apellido)






def clearall():
    pantalla.set("")
    pantalla2.set("")
    datos.set("")

entry  = Entry (root, textvariable=pantalla)
entry.grid (row= 1, column= 2) 

entry2  = Entry (root, textvariable=pantalla2)
entry2.grid (row= 2, column= 2 ) 

nombre = Button(root, text="establecenombre", )
nombre.grid(row= 1 , column= 1 )

apellido = Button(root, text="establecenombre", )
apellido.grid(row = 2 , column= 1 )


#obtener datos 

obtenerdatos = Button(root, text="obtener_datos", command=getdatos)
obtenerdatos.grid(row= 4, column= 1 )

entry  = Entry (root, textvariable=datos)
entry.grid (row= 4, column= 2) 

#limpiar 

clear = Button(root, text="limpiar todo ", command=clearall)
clear.grid(row= 6, column= 1 , columnspan=2)


root .mainloop () 