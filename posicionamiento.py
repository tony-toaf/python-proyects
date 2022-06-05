from os import lseek
from readline import insert_text
from tkinter import *
def sumar():
    numero1=entry.get()
    numero2= entry1.get()

    resultado = numero1 + numero2

    entry2.insert(resultado)




    

   

 
root = Tk()
root.config(width=400, height=400, bg= "black")

label = Label(root, text="primer valor")
label.place(x=30, y=40)

entry = Entry(root, width=20)
entry.place(x=200, y=40)


label1 = Label(root, text="segundo valor")
label1.place(x=30, y=80)

entry1 = Entry(root, width=20)
entry1.place(x=200, y=80)


label2 = Label(root, text="resultado")
label2.place(x=30, y=200)

entry2 = Entry(root, width=20)
entry2.place(x=200, y=200)


botonr = Button(root, text="get_resultado", command=sumar)
botonr.place(x=200, y=350)



root.mainloop()