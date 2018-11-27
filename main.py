#main
import pygame as pg
import random
from settings import *
from sprites import *

class Game:
	def __init__(self): #initialize game window
		pg.init() #initialize pygame
		pg.mixer.init() #initialize pygame sounds
		self.screen = pg.display.set_mode((WIDTH,HEIGHT)) #create screen
		pg.display.set_caption(TITLE) #set window title
		self.clock = pg.time.Clock() #create clock
		self.running = True #set run loop to true
		
	def new(self): #resets the game
		self.all_sprites = pg.sprite.Group()
		self.player = Player()
		self.all_sprites.add(self.player)
		self.run()
		
	def run(self): #game loop
		self.playing = True
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()
		
	def events(self): #game loop - events
		for event in pg.event.get():
			if event.type == pg.QUIT: #check for QUIT
				self.playing = False
				self.running = False
	
	def update(self): #game loop - update
		self.all_sprites.update()
		
	def draw(self): #game loop - draw
		self.screen.fill(BLACK)
		self.all_sprites.draw(self.screen)
		pg.display.flip() #*after* drawing everything, flip the display
		
	def show_start_screen(self): #show start screen
		pass
		
	def show_go_screen(self): #show game over screen
		pass
		
g = Game()
g.show_start_screen()
while g.running:
	g.new()
	g.show_go_screen()
	
pg.quit()