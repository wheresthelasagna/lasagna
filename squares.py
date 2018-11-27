import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock() #create the clock

pygame.init() #initiate pygame

pygame.display.set_caption('things') #set title

window_size = (500,500) #set window size

screen = pygame.display.set_mode(window_size,0,32) #initiate the window

player_image = pygame.transform.scale(pygame.image.load('pupper_bread.gif'),(100,100)) #create an image

moving_right = False
moving_left = False
moving_up = False
moving_down = False

player_location = [0,0]
player_y_momentum = 0

player_rect = pygame.Rect(player_location[0],player_location[1],player_image.get_width(),player_image.get_height())
test_rect = pygame.Rect(100,100,100,100)

while True: #game loop
	screen.fill((0,0,0))
	
	screen.blit(player_image,player_location)
	
	#gravity
	"""
	if player_location[1] > window_size[1]-player_image.get_height():
		player_y_momentum = -player_y_momentum
	else:
		player_y_momentum += 0.2
	player_location[1] += player_y_momentum
	"""
	
	if moving_right == True:
		player_location[0] += 4
	if moving_left == True:
		player_location[0] -= 4
	if moving_up == True:
		player_location[1] -= 4
	if moving_down == True:
		player_location[1] += 4
	
	player_rect.x = player_location[0]
	player_rect.y = player_location[1]
	
	if player_rect.colliderect(test_rect):
		pygame.draw.rect(screen,(255,0,0),test_rect)
	else:
		pygame.draw.rect(screen,(0,255,0),test_rect)
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				moving_right = True
			if event.key == K_LEFT:
				moving_left = True
			if event.key == K_UP:
				moving_up = True
			if event.key == K_DOWN:
				moving_down = True
		if event.type == KEYUP:
			if event.key == K_RIGHT:
				moving_right = False
			if event.key == K_LEFT:
				moving_left = False
			if event.key == K_UP:
				moving_up = False
			if event.key == K_DOWN:
				moving_down = False
				
	pygame.display.update() #update display
	clock.tick(60) #maintain 60 fps