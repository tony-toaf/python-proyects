import pygame
pygame.init()

zise =(400, 500) #tamagano de la ventana

#area colores 

black=(0,0,0)
white =(255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)


#windows creatror 
#windows = pygame.display.set_mode(zise)
windows = pygame.display.set_mode((600, 600))

while True:  #creacon de la ventana
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			sys.exit()