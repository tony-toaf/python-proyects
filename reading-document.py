
documen = open("document.txt", "r")
asing = documen.read()
listaword = asing.split()

charterfind = 0 




for i in listaword:

	if(i=="una"):
		chater=i
		charterfind = True


if charterfind:
	print("valor encontrado")
	
else:
	print("no find try again")



