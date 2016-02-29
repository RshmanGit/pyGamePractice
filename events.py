import pygame, sys
from pygame.locals import *

bif = "bg.jpg"
mif = "sprite.png"

pygame.init()
screen = pygame.display.set_mode((1260,720),0,32) #created a 32 bit screen with the given resolution

background = pygame.image.load(bif).convert()
sprite = pygame.image.load(mif).convert_alpha()

#events
x,y = 0,0
movex, movey = 0,0

while True:

	for event in pygame.event.get(): #this statement goes through all the events created
		if event.type == QUIT: #QUIT is a predefined method
			pygame.quit()
			sys.exit()

		if event.type == KEYDOWN: #this goes through all the keyboard events 
			if event.key == K_LEFT: #this event activates when the left key is pressed
				movex=-1
			elif event.key == K_RIGHT: #this event activates when the right key is pressed
				movex=+1
			elif event.key == K_UP: #this event activates when the left key is pressed
				movey=-1
			elif event.key == K_DOWN:
				movey=+1

		if event.type == KEYUP:
			if event.key == K_LEFT: #this event activates when the left key is pressed
				movex=0
			elif event.key == K_RIGHT: #this event activates when the right key is pressed
				movex=0
			elif event.key == K_UP: #this event activates when the left key is pressed
				movey=0
			elif event.key == K_DOWN:
				movey=0

	x+=movex
	y+=movey

	screen.blit(background,(0,0))
	screen.blit(sprite,(x,y))

	pygame.display.update()