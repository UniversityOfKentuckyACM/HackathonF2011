from State import State
import pygame
import pygame.gfxdraw
import util
from pygame.locals import *

class GameState(State):
	def __init__(self, main):
		# transition from another state
		State.__init__(self,main)
		
		self.bgGroup = pygame.sprite.OrderedUpdates()
		self.playerGroup = pygame.sprite.RenderPlain()
	
	def __del__(self):
		# transition to another state
		pass
		
	def loadPlayer(self, imagefile):
		self.player = Actor(imagefile, -1)
		self.playerGroup.add(self.player)
		return self.player
	
	def update(self):
		self.checkCollisions()
		State.update(self);
	
	def handleEvent(self):
		# For each event that occurs this frame
		for event in pygame.event.get():
			# If user exits the window
			if event.type == QUIT:
				sys.exit(0)

			# handle mouse
			
			# monitor keyboard
			self.handleKey(event)
		
	def handleKey(self, event):
		# handle keyboard keys
		'''
			Handle input from user keyboard
		'''
		if event.type == pygame.KEYDOWN:
			# exit game
			if event.key == K_ESCAPE:
				sys.exit(1)

		elif event.type == pygame.KEYUP:
			pass
			
	def checkCollisions(self):
		pass
		
	def draw(self):
		# draw background
		self.bgGroup.draw(self.main.screen)
		# draw player	
		self.playerGroup.draw(self.main.screen)
		
		State.draw(self)
