#scrip para crear punto de wifi  falso 
import os
##_______lista de paramtros 1si, 0no
os.system("clear")

monitor_mode= input("inciar modo monitor(1, 0)>>>> ")
hostapd = input ("Crear archivo hostapd.conf (1, 0)>>>> " )
dnsmaspq =input ("Crear archivo dnsmasq.conf (1, 0)>>>> " )
enrutamiento =input ("Crear tabla de enrrutamiento (1, 0)>>>> " )
firewall= input("configurar firewall(1, 0)>>>> ")


nombre_tarjeta = " "

if hostapd=="1":
	print("Creando el documento dnsmasq.conf...........")
	print("") #creacion de dnsmaq.conf
	dnsmasqfile = open("dnsmasq.conf", "w")
	print("dnsmasq.conf creado con exito")
	print(" ")
	print("agnadiendo parametros del archivos...")
	print(" ")
	nombre_tarjeta = input("nombre de la interfas >>> ")

	lista_parametros = ["dhcp-range=192.168.1.2,192.168.1.30,255.255.255.0,12h\n", "dhcp-option=3,192.168.1.1\n", 
	"dhcp-option=6,192.168.1.1\n","server=8.8.8.8\n", "log-queries\n","log-dhcp\n","listen-address=127.0.0.1"]

	dnsmasqfile.write("interfase="+nombre_tarjeta+"\n")

	for i in lista_parametros:
		dnsmasqfile.write(i)
	print("archivo gerado")

#----------------------------------creacion de fils hostapd-------------
if dnsmaspq=="1":
	print("genarando archivos hostapd........")
	hostapdfile = open("hostapd.conf","w")

	print("agnadiendo parametros a hostapd.conf\n")

	hostapdfile.write("interface="+nombre_tarjeta+"\n")

	lista_parametros_hostapd=["ssid=internet\n","hw_mode=g\n",
	"channel=05\n","macaddr_acl=0\n","auth_algs=1\n","ignore_broadcast_ssid=0\n",
	"ieee80211n=1\n","wme_enabled=1\n"]

	for i in lista_parametros_hostapd:
		hostapdfile.write(i)
	print("archivo gerado")
#------------iniciar modo monitor-----
if monitor_mode  == "1":
	os.system("iwconfig")
	interfase_name = input("interfase name>>> ")
	os.system("sudo -S su")
	os.system ("sudo  -S airmon-ng "+interfase_name)

#---------cracion de anrutamiento-----

if enrutamiento == "1":
	os.system("route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1")
	print("enrutamiento generado")

#-----------configuracion del firewall-------
if firewall == "1":
	
	os.system("iptables --table nat --append 	POSTROUTING --out-interface wlan0 -j MASQUERADE")
	tarjeta_salida_internet=input("nombre tarjeta de salida de intenet: ")
	os.system("iptables --append FORWARD --in-interface "+tarjeta_salida_internet)
	os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
	print("paquetes desabilitados ")	

else:
	print("finalizado")











