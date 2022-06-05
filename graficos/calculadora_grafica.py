from __future__ import division
from tkinter import *
root = Tk()
root.title("Calculadora by Toaf")
root.resizable(False, False)
frame = Frame (root, width=400 ,height=400)
frame.config(bg="black")
frame.pack()

#area de variables 
numeropantalla = StringVar()
operaciones = ""
resultado=0
reset_pantalla= False

def suma(numero):
    global operaciones  

    global reset_pantalla

    global  resultado 

    resultado += int(numero)

    numeropantalla.set(resultado)

    reset_pantalla = True

    operaciones = "suma"

#divicon funcion 

def mult (numero):

    global resultado 

    global operaciones 

    global reset_pantalla 

    resultado = int(numero)


    operaciones = "multiplicacion"

    reset_pantalla = True

#funcion dividir 
def div (numero):

    global resultado 

    global operaciones 

    global reset_pantalla 

    resultado = int(numero)


    operaciones = "divicion"

    reset_pantalla = True

def igual(numero):
    global operaciones

    global resultado 

    if operaciones == "suma":
    
        numeropantalla.set(resultado + int(numero))

        reset_pantalla = True

        operaciones = ""

    if  operaciones == "multiplicacion":

        numeropantalla.set(resultado * int(numero))

        operaciones = ""

        reset_pantalla = True

    if  operaciones == "divicion":
    
        numeropantalla.set(resultado / int(numero))

        operaciones = ""

        reset_pantalla = True

    #funcion en panlla 

    if numeropantalla.get("8669"):
        limpiar()
        numeropantalla.set("calculadora version 1 by tony alonzo")
        




def npulsado(numero):

    global reset_pantalla 

    global operaciones 

    global resultado 

    if reset_pantalla != False:
        numeropantalla.set(numero)
        reset_pantalla  =  False
    else:

        numeropantalla.set(numeropantalla.get()+  numero)

def limpiar():
    global reset_pantalla

    global operaciones

    global resultado

    numeropantalla.set("")

    resultado =0
    
    reset_pantalla = False

    operaciones = ""

#funcion de informacion 




#ventamna principal 
pantalla = Entry(frame, width=35, textvariable= numeropantalla)
pantalla.grid(pady= 3,row=1 , column= 1 , columnspan=5)

#botones de acciones principales
bsuma= Button(frame, text= "+", width=5, height=2, command=lambda:suma(numeropantalla.get()))
bsuma.grid(padx=2,row= 2 ,column=4)

bresta= Button(frame, text= "-", width=5, height=2)
bresta.grid(row= 3 ,column=4)

bmult= Button(frame, text= "*", width=5, height=2, command=lambda:mult(numeropantalla.get()))
bmult.grid(row= 4 ,column=4)

bdiv= Button(frame, text= "/", width=5, height=2, command=lambda:div(numeropantalla.get()))
bdiv.grid(row= 5 ,column=4)

bcero= Button(frame, text= "0", width=5, height=2)
bcero.grid(row= 5 ,column=1)

breset= Button(frame, text= "C", width=5, height=2, command=limpiar)
breset.grid(row= 5 ,column=2)


bigual= Button(frame, text= "=", width=5, height=2, command=lambda:igual(numeropantalla.get()))
bigual.grid(row= 5 ,column=3)

#area de botones "s

#linea primera 
numero7 = Button (frame, text= "7", width=5, height=2, command=lambda:npulsado("7"))
numero7.grid(padx=2,pady = 2,row=2, column= 1)

numero8 = Button (frame, text= "8", width=5, height=2, command=lambda:npulsado("8"))
numero8.grid(padx=2,pady = 2, row=2, column= 2)

numero9 = Button (frame, text= "9", width=5, height=2, command=lambda:npulsado("9"))
numero9.grid(padx=2,row=2, column= 3)

#linea segunda 
numero6 = Button (frame, text= "6", width=5, height=2, command=lambda:npulsado("6"))
numero6.grid(padx=2,row=3, column= 1)

numero5 = Button (frame, text= "5", width=5, height=2, command=lambda:npulsado("5"))
numero5.grid(padx=2,row=3, column= 2)

numero4 = Button (frame, text= "4", width=5, height=2, command=lambda:npulsado("4"))
numero4.grid( padx=2,row=3, column= 3)


#linea tercera 
numero3 = Button (frame, text= "3", width=5, height=2, command=lambda:npulsado("3"))
numero3.grid(padx=2,row=4, column= 1)

numero2 = Button (frame, text= "2", width=5, height=2, command=lambda:npulsado("2"))
numero2.grid(padx=2,pady = 2,row=4, column= 2)

numero1 = Button (frame, text= "1", width=5, height=2, command=lambda:npulsado("1"))
numero1.grid(padx=2, pady = 2,row=4, column= 3)



root.mainloop()