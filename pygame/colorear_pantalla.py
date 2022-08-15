import pygame
pygame.init()

zise =(400, 500) #tamagano de la ventana

#area colores 

black=(0,0,0)
white =(255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)


#
windows = pygame.display.set_mode(zise)

while True:  #creacon de la ventana
	for event in pygame.event.get():
		#print(event)
		if event.type == pygame.QUIT:
			Sys.exit()

		circulo = pygame.draw.circle(windows, red, (200, 200), 100)
		#establecer colores nota tiene que ir fuera del condicional
		windows.fill(red)

		windows.fill(circulo)

		#pygame.draw.line(windows, white, [20,250] , [390,1], 20 )

		#pygame.draw.circle(windows, red, (200, 200), 100) 

		#pygame.draw.polygon(windows, white, [100, 200, 20, 40])


		#update windows
		pygame.display.flip()

