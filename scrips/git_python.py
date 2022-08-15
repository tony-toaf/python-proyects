#-------scrip para minimizar uso de git en linux-----------
#version 1.0  by TONY-TOAF
#date -17-07-2022
import os
os.system("clear")

def nombre():
	print(" _____ ___    _    _____      ___   __   ")
	print("|_   _/ _ \  / \  |  ___|    ( _ ) / /_  ")
	print("  | || | | |/ _ \ | |_ _____ / _ \| '_ \ ")
	print("  | || |_| / ___ \|  _|_____| (_) | (_) |")
	print("  |_| \___/_/   \_\_|        \___/ \___/ ")
nombre()

print("------------------- by TONY-TOAF----------------------------")
show_options_user = input("show options (1,0)>>> ")
push = input("push files (1,0)>> ")
add = input("add files (1,0)>> ")
commit = input("commit to files (1,0)>> ")
status = input("status of files (1,0)>> ")
init = input("iniciar files (1,0)>> ")
general = input("all options (1,0)>> ")

lista_opsion= [ init, add, commit, status, general]
lista_opsion

if show_options_user == "1":
	print("\nuser= tony-toaf\n")
	print("token= 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\n")
if init == "1":
	#os.system("git init")
	print("repositorio iniciado")

if add == "1":
	os.system("git add *")
	print("archivos agnadidos")

if status == "1":
	os.system("git status")

if commit=="1":
	nombre_commit = input("commit text: ")
	os.system("git commit -m"+nombre_commit)

if push == "1":
	try:
		os.system("git push")
	except fatal:
		print("no se pudo ejecutar")
	else:
		os.system("git push")
	finally:
		print("")


		
 	