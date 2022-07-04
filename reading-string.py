nombre = ['tony', 'omar', 'alonzo']
varlor = 0

for i in nombre:
	if(i=="tony"):
		chater=i
		varlor = True


if varlor:
	print("valor encontrado")
	file = open("letras.txt", "a")
	file.write(('\n'+chater))
	file.close()
else:
	print("no find try again")
