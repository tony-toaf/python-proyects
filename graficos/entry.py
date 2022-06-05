from logging import root
from sqlite3 import Row
from string import hexdigits
from tkinter import *
from turtle import width

root = Tk()
root.title("calculadora")
root.resizable(False, False)
root.geometry('300x300')

entry =Entry(root, width= 35,insertborderwidth=100 )
entry.grid(row=1 , column =1 )



root.mainloop()