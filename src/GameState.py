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

IMG_HUD = "hud_bg.png"
IMG_SLOT = "slot_bg.png"
IMG_HEART = "hud_health.png"
IMG_HEART_HALF = "hud_health_half.png"

class GameState(State):
	'''
		State for game playing mode.
	'''
	
	bgGroup = pygame.sprite.OrderedUpdates()
	playerGroup = pygame.sprite.RenderPlain()
	guiGroup = pygame.sprite.OrderedUpdates()

	def __init__(self, main):
		# transition from another state
		State.__init__(self,main)
		self.loadPlayer()
		self.hud = Actor(IMG_HUD,-1)
		self.hud.setPos(WIDTH/2,HEIGHT-100)
		GameState.guiGroup.add(self.hud)
		self.health = 7
		self.hudHearts = []
		self.hudSlot = [None]*3
		
		for i in range(0,3):
			self.hudSlot[i] = Actor(IMG_SLOT,-1)
			self.hudSlot[i].setPos(115 + i*115, HEIGHT-100)
			self.guiGroup.add(self.hudSlot[i])
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
		
		self.updateHud()
		
		GameState.guiGroup.update()
		GameState.playerGroup.update()
		
	def updateHud(self):
		full = self.health/2
		halve = self.health%2
		
		if len(self.hudHearts) != full+halve:
			while len(self.hudHearts) < full:
				self.hudHearts.append(Actor(IMG_HEART,-1))
				GameState.guiGroup.add(self.hudHearts[-1])
				
			while len(self.hudHearts) > full:
				GameState.guiGroup.remove(self.hudHearts.pop())
			
			if halve == 1:
				self.hudHearts.append(Actor("hud_health_half.png",-1))
				GameState.guiGroup.add(self.hudHearts[-1])
				
			for i in range(0,full+halve):
				self.hudHearts[i].setPos(WIDTH-60-i*60,HEIGHT-50)
				print i, (WIDTH-60-i*60,HEIGHT-50)
				
	
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
		
		# draw gui
		GameState.guiGroup.draw(self.main.screen)
		
		# flip screen
		State.draw(self)
