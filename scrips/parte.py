from os import system

print("--------------------------------Parte UNAS----------------------------------")

lista = ["1.....grupo 1 de fin de semana", "2......grupo 2 de fin de semana","3.......Parte de dia de semana"]

#lista del grupo 1
listg1 = ["S/O Lenar Sánchez", "C/I David Ortiz", "C/I Mauricio Manueles", "A/P Darwin Flores","A/P Eris Avila","A/P Enrique González",
"A/P Brayan Izaguirre", "A/P Evelyn Cañada","A/P Kevin Matamoros","A/P Saul Irias", "A/P Kevin Godoy"]
#lista del grupo 2
listg2 = [" S/C Erick González","C/I Edwin Funez ","C/I Selvin Medina ","C/I Carlos Ledesma ","A/P Miguel Castellanos ","A/P Nancy Cruz ", "A/P Edar Fonseca",
"A/P Adalid Corea","A/P Alex Betanco ","A/P Carlos Sosa","A/P Tony Alonzo"]

listgeneral = ["S/C Erick González","S/O Lenar Sánchez","C/I Edwin Funez ", "C/I David Ortiz", "C/I Selvin Medina ","C/I Carlos Ledesma ", #lista general
"C/I Mauricio Manueles", "A/P Darwin Flores","A/P Eris Avila","A/P Enrique González","A/P Edar Fonseca","A/P Nancy Cruz ","A/P Brayan Izaguirre",
 "A/P Evelyn Cañada","A/P Adalid Corea","A/P Kevin Matamoros","A/P Saul Irias", "A/P Kevin Godoy","A/P Alex Betanco ","A/P Carlos Sosa","A/P Tony Alonzo"]

lDisponibles = []
lServicios=[]
lvacaciones = []
lmpais = []
lmciudad = []
ldescansando = []
lcurso = []

for i in lista:
	print(i)

seleccion = input("realiza tu eleccion: ")
print("\n")

if (seleccion == "1"):
	numero = 1
	for i in listg1:
		print(numero , i) #imprimiendo en orden numerico g1 fin
		numero+=1 #grupo 1 de fin
	
		


elif (seleccion == "2"):
	numero = 1
	for i in listg2:
		print(numero , i) #imprimiendo en orden numerico g2 fin
		numero+=1


elif (seleccion == "3"):
	numero = 0  
	for i in listgeneral: #imprimiendo el personal
		print(numero, i)
		numero +=1


	for i in range(1,22):
		seleccion =input('\nseleccione los Disponibles para agregar, "enter" para finalizar: ')  #anadiendo los disponibles
		if (seleccion == ""):
			print("programa finalizado")
			break
		else:
			lDisponibles.append(int(seleccion))


	for i in range(1,22):
		seleccion =input('\nseleccione los Servicios para agregar, "enter" para finalizar: ')  #anadiendo los Servicios
		if (seleccion == ""):
			print("programa finalizado")
			break
		else:
			lServicios.append(int(seleccion))


	for i in range(1,22):
		seleccion =input('\nseleccione los Mision Ciudad para agregar, "enter" para finalizar: ')  #anadiendo los Mision Ciudad
		if (seleccion == ""):
			print("programa finalizado")
			break
		else:
			lmciudad.append(int(seleccion))

	for i in range(1,22):
		seleccion =input('\nseleccione los Mision Pais para agregar, "enter" para finalizar: ')  #anadiendo los mision pais
		if (seleccion == ""):
			print("programa finalizado")
			break
		else:
			lmpais.append(int(seleccion))


	for i in range(1,22):
		seleccion =input('\nseleccione los Vacaciones para agregar, "enter" para finalizar: ')  #anadiendo los vacaciones
		if (seleccion == ""):
			print("programa finalizado")
			break
		else:
			lvacaciones.append(int(seleccion))

	for i in range(1,22):
		seleccion =input('\nseleccione los Descansando para agregar, "enter" para finalizar: ')  #anadiendo los Descansando
		if (seleccion == ""):
			print("programa finalizado")
			break
		else:
			ldescansando.append(int(seleccion))


	for i in range(1,22):
		seleccion =input('\nseleccione los en Curso para agregar, "enter" para finalizar: ')  #anadiendo los curso 
		if (seleccion == ""):
			print("programa finalizado")
			break
		else:

			lcurso.append(int(seleccion))

	system("clear")
	#-----------------impresiones de terminos----------------------
	agente = input("nombre del agente de Servicio: ")
	fecha = input("fecha en (Dia- fecha: eje Lunes 04 de Enero:   ")
	novedades = input("Pega las novedades de importancia durante el dia: ")  #pidiendo las novedades de importancia
	print("\n")
	print(fecha)
	print("\n🇭🇳 REPÚBLICA DE HONDURAS 🇭🇳")
	print("SECRETARIA DE SEGURIDAD")
	print("DIRECCIÓN POLICIAL DE INVESTIGACIÓNES")
	print("UNIDAD NACIONAL ANTISECUESTRO")
	print("\n")
	print(fecha)

	print("\n*Disponibles*") #sacando los valores impresos de disponibles
	n=1
	for i in lDisponibles:
		print(n, listgeneral[i])
		n+=1

	print("\n*Servicios*") #sacando los valores impresos de disponibles
	n=1
	for i in lServicios:
		print(n, listgeneral[i])
		n+=1	

	print("\n*Mision Ciudad*") #sacando los valores impresos de vacaciones
	n=1
	for i in lmciudad:
		print(n, listgeneral[i])
		n+=1

	print("\n*Mision Pais*") #sacando los valores impresos de vacaciones
	n=1
	for i in lmpais:
		print(n, listgeneral[i])
		n+=1


	print("\n*Vacaciones*") #sacando los valores impresos de vacaciones
	n=1
	for i in lvacaciones:
		print(n, listgeneral[i])
		n+=1

	print("\n*Descansando*") #sacando los valores impresos de vacaciones
	n=1
	for i in ldescansando:
		print(n, listgeneral[i])
		n+=1


	print("\n*Curso*") #sacando los valores impresos de vacaciones
	n=1
	for i in lcurso:
		print(n, listgeneral[i])
		n+=1

	#-------------------area de novedades de importancia--------------------------------
	print("\n")
	print ("*Novedades de importancia*")
	print(novedades,"\n")
	print ("*Dios    Patria   Servicio*\n")
	print("Agente de Policia")
	print(agente)
	print("Servicio-UNAS-SPS")














