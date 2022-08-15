from ast import LtE
from heapq import heapify
from http.client import PAYMENT_REQUIRED
from logging import lastResort
from socket import J1939_MAX_UNICAST_ADDR
from tkinter import *
from tkinter.tix import ROW
root = Tk()
frame = Frame()
frame.pack()
root.title("base de datos alumnos")
root.geometry("780x500")

Nombre = Label(frame, text="NOMBRE", justify=LEFT)  
Nombre.grid(row= 1 , column= 0, pady=10)
Apellido = Label(frame, text="APELLIDO", justify=LEFT)  
Apellido.grid(row= 2 , column= 0, pady=10, padx=2)
Edad = Label (frame, text="EDAD", justify=LEFT)
Edad.grid(row=3, column=0, pady=10)
Fnacimiento = Label(frame, text="FECHA NACIMIENTO", justify=LEFT)  
Fnacimiento.grid(row= 4 , column= 0, pady=10)


#area de texto 
ltext = Label(frame, text="INFORMACION", justify=LEFT)
ltext.grid(row=2, column=3, padx=5) 
binformacion = Button(frame, text="GET-INFORMACION")
binformacion.grid(row=1, column=4, pady=5)
T = Text(frame, width=20, height=10,)
T.grid(row=2, column=4, pady=30)


#creacion de los entrys 
eNombre = Entry(frame)
eNombre.grid(row=1 , column= 1) #nombre 

eApellido = Entry(frame)
eApellido.grid(row=2 , column= 1) #apellido 

eEdad = Entry(frame)
eEdad.grid(row=3 , column= 1) #edad

Efnacimiento = Entry(frame)
Efnacimiento.grid(row=4 , column= 1) #fecha nacimient 

ematerias = Entry(frame)
ematerias.grid(row=4, column= 1) #materias


#AREA IFORMACION   

#area de botones de crud
C = Button(frame, text="CREAR")
C.grid(row=6, column=1) #crate 

R = Button(frame, text="RELOAD")
R.grid(row=6, column=3) #read

U = Button(frame, text="UPDATE")
U.grid(row=6, column=2) #crate

D = Button(frame, text="DELETE")
D.grid(row=6, column=4) #updateCREAR


root.mainloop()