nombre = "Tony omar alonzo figuero"

listaNombre = nombre.split()
valor = 0

for i in listaNombre:
	if(i=="tony") or (i=="Tony"):
		valor = True

if valor:
	print("el nombre coincide")
else:
	print("nombre no coincide")