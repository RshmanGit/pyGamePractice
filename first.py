import pygame, sys
from pygame.locals import *

bif = "bg.jpg"
mif = "sprite.png"

pygame.init()
screen = pygame.display.set_mode((1260,720),0,32) #created a 32 bit screen with the given resolution

background = pygame.image.load(bif).convert()
sprite = pygame.image.load(mif).convert_alpha()

while True:
	for event in pygame.event.get(): #it is an event handler to shut down the program
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	screen.blit(background, (0,0)) #it basically pastes the background into the screen

	x,y = pygame.mouse.get_pos()
	x -= sprite.get_width()/2 #it puts the position of the mouse right into the middle of the image
	y -= sprite.get_height()/2

	screen.blit(sprite, (x,y))

	pygame.display.update()