#!/usr/bin/python

# Python includes
import sys

# Pygame includes
import pygame
from pygame.locals import *

# Game includes
from Graphics import Graphics
from Vector2 import Vector2
from config import *

class Game():
	def __init__(self):
		self.g = Graphics(self)

		# load background image
		#self.g.loadBackground(BACKGROUND_IMAGE)

		# Initialize our player and set its position to (50,50)
	#	self.player = self.g.loadPlayer(PLAYER_IMAGE)
		#self.player.setPos(START_X, START_Y)

		# game clock
		self.clock = pygame.time.Clock()

		# game state
		self.state = PLAY

		# Loop until exit
		self.gameLoop()
	
	def gameLoop(self):

		while True:
			# ensure we're running at a stable FPS
			self.clock.tick(FRAME_RATE)

			# State machine
			if self.state == START_MENU:
				self.startMenu()

			elif self.state == PLAY:
				self.playFrame()

	def startMenuFrame(self):
		# Grab input from start menu
		self.startMenuInput()

		# Update menu choice
		self.g.startUpdate()

		# draw start menu
		self.g.drawStartMenuScreen()
	
	def playFrame(self):
		# Move character around, etc
		self.handlePlayInput()

		# Update all player, AI, etc
		self.g.playUpdate()

		# Draw play screen
		self.g.drawPlayScreen()
	
	def startMenuInput(self):
		'''
			Handle input concerning start menu screen
		'''
		pass

	def handlePlayInput(self):
		'''
			Handle all input from user. This includes keypresses, mouse clicks,
			exiting, etc.
		'''
		# For each event that occurs this frame
		for event in pygame.event.get():
			# If user exits the window
			if event.type == QUIT:
				sys.exit(0)

			# handle mouse
			
			# monitor keyboard
			self.handlePlayKeys(event)

	
	def handlePlayKeys(self, event):
		'''
			Handle input from user keyboard
		'''
		if event.type == pygame.KEYDOWN:
			# exit game
			if event.key == K_ESCAPE:
				sys.exit(1)

		elif event.type == pygame.KEYUP:
			pass

if __name__ == '__main__':
	g = Game()
