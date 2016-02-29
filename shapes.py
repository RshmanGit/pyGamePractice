import pygame,sys
from pygame.locals import *

bif = "bg.jpg"

pygame.init()
screen = pygame.display.set_mode((1260,720),0,32)

background = pygame.image.load(bif).convert()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()


	screen.blit(background,(0,0))
		
	screen.lock()
	pygame.draw.rect(screen, (140,240,130), Rect((100,100),(130,170)))
	screen.unlock()

	
	pygame.display.update()