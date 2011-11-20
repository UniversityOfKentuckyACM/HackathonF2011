import pygame
import pygame.gfxdraw
from pygame.locals import *

import util
import sys
import math

from State import State
from Actor import Actor
from Player import Player
from Vector2 import Vector2
from TerrainLayer import TerrainLayer
from config import *

class GameState(State):
	'''
		State for game playing mode.
	'''
	
	bgGroup = pygame.sprite.OrderedUpdates()
	playerGroup = pygame.sprite.RenderPlain()
	

	def __init__(self, main):
		# transition from another state
		State.__init__(self,main)

		self.loadPlayer()
		self.background = TerrainLayer("d1_0_0.map")

	def __del__(self):
		# transition to another state
		pass
		
	def loadPlayer(self):
		self.player = Player()
		GameState.playerGroup.add(self.player)
	
	def update(self):
		self.checkCollisions()
		State.update(self);

		GameState.playerGroup.update()
	
	def handleEvent(self):
		# handle mouse
		mousePos = Vector2(pygame.mouse.get_pos())
		self.player.orient(mousePos)
			
		# For each event that occurs this frame
		for event in pygame.event.get():
			# If user exits the window
			if event.type == QUIT:
				sys.exit(0)

			# monitor keyboard
			self.handleKey(event)
		
	def handleKey(self, event):
		'''
			Handle input from user keyboard
		'''
		if event.type == pygame.KEYDOWN:
			# exit game
			if event.key == K_ESCAPE:
				sys.exit(1)
			if event.key == MOVEMENT_KEYS[0]:
				self.player.move(0)
			if event.key == MOVEMENT_KEYS[1]:
				self.player.move(1)
			if event.key == MOVEMENT_KEYS[2]:
				self.player.move(2)
			if event.key == MOVEMENT_KEYS[3]:
				self.player.move(3)

		elif event.type == pygame.KEYUP:
			if event.key == MOVEMENT_KEYS[0]:
				self.player.unMove(0)
			if event.key == MOVEMENT_KEYS[1]:
				self.player.unMove(1)
			if event.key == MOVEMENT_KEYS[2]:
				self.player.unMove(2)
			if event.key == MOVEMENT_KEYS[3]:
				self.player.unMove(3)
			
	def checkCollisions(self):
		pass
		
	def draw(self):
		#draw background
		#self.main.screen.blit(self.background, self.background.get_rect())
		self.background.drawTerrain(self.main.screen);	

		# draw player	
		GameState.playerGroup.draw(self.main.screen)
		
		# flip screen
		State.draw(self)
