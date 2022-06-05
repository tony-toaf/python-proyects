#calaculadora stylo consola solo terminal python funciones basicas
#by Tony Alonzo
#date 08-05-2022

from audioop import mul
from xml.etree.ElementPath import ops


numero1 = int(input("introduce un numero>>>>> "))

numero2 = int(input("introduce un segundo valor>>>> "))

resultado = 0 

def opciones():
    print("1...sumar")
    print("2...restar")
    print("3...multiplicar")
    print("4...dividir")



def sumar():
    resultado = numero1 + numero2
    print(resultado)

def restar():
    resultado = numero1 + numero2
     print (resultado)

def multiplicar():
    resultado = numero1 * numero2
     print(resultado)
def dividir():
    resultado = numero1 / numero2
    print(resultado)

    


print(opciones())

own = int(input("escriba el numero de su eleccion>>>>>>  "))

if own == 1 :

    print(sumar())
elif own == 2: 
    print(restar())
elif own == 3: 
    print(multiplicar())
else:
    print(dividir())
