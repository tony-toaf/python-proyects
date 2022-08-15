'''for i in range (0,10,2):
	print("la imprecion es ", str(i))'''
import os
import argparses

#ejemplo de tabla de multiplicar 

#tabla = int(input("introduce la tabla a multiplicar: "))

pwd = os.getcwd()
print(pwd)
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'


BLUE = '\33[94m'

print(BLUE)

parser = argparse.ArgumentParser(description=f'{RED}APK Infector v1.0')

print(parser)