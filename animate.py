import pygame,sys
from pygame.locals import *

bif = "bg.jpg"
mif = "sprite.png"

pygame.init()
screen = pygame.display.set_mode((1260,720),0,32)

background = pygame.image.load(bif).convert()
sprite = pygame.image.load(mif).convert_alpha()

x=0
clock = pygame.time.Clock()
speed = 250
frame = 0

while True:
	frame += 1
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	screen.blit(background,(0,0))
	
	screen.blit(sprite, (x, 160))
	milli = clock.tick()
	seconds = milli/1000.

	dm = seconds*speed
	x+=dm

	if clock.tick == milli+1000 :
		print str(frame) + "frames per second"
		frame = 0

	if x>1080:
		x=0



	pygame.display.update()