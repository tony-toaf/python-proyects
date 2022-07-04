cadena = "Pues hemos llegado"
lista = []


contadospacios = 0

for i in cadena:
	if (i == " "):
		contadospacios +=1


valortotal = (len(cadena)-contadospacios)

print(valortotal)