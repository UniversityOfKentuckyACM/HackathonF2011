
# Graphics class
# Contains screen, sprite groups, etc
import pygame
import pygame.gfxdraw
import util

import random

from Actor import Actor
from Vector2 import Vector2

from config import *
from pygame.locals import *
		
	
class Graphics():
	'''
		Graphics engine.
	'''
	def __init__(self, game_obj):
		self.main = game_obj
		
		# create screen
		if IS_FULLSCREEN:
			self.screen = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN|DOUBLEBUF)
		else:
			self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		
		pygame.display.set_caption(GAME_TITLE)
	
		# Add more groups if necessary
		self.bgGroup = pygame.sprite.OrderedUpdates()
		self.playerGroup = pygame.sprite.RenderPlain()

	# TODO
	def loadPlayer(self, imagefile):
		self.player = Actor(imagefile, -1)
		self.playerGroup.add(self.player)
		return self.player
	
	def startUpdate(self):
		'''
			Update information on start menu
		'''
		pass
	
	def drawStartMenuScreen(self):
		'''
			Draw start menu
		'''
		pass

	def playUpdate(self):
		''' 
			Update play screen
		'''
		self.bgGroup.update()
		self.playerGroup.update()

		self.checkCollisions()

	def drawPlayScreen(self):
		# draw background
		self.bgGroup.draw(self.screen)
		# draw player	
		self.playerGroup.draw(self.screen)

		pygame.display.flip()

	def checkCollisions(self):
		# For each collision between two groups, kill them both.
		# the 1,1 tells pygame to kill both. If for instance we wanted to only kill the torpedo 1,0 would suffice.
		#for hit in pygame.sprite.groupcollide(self.torpedoGroup, self.subGroup, 1, 1):
		pass

