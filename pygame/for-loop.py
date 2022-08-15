import pygame
pygame.init()

zise =(600, 600) #tamagano de la ventana

#area colores 

black=(0,0,0)
white =(255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)



windows = pygame.display.set_mode(zise)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Sys.exit(	)
			
		
		windows.fill(white)

		for i in range(20, 800, 70):
			pygame.draw.rect(windows, black,(i, 300,30, 50 ))

			pygame.draw.line(windows, black, (i, 250), (i, 100), 50)

	


		#update windows
		pygame.display.flip()