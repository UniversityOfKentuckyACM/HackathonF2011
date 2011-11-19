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

		# Loop until exit
		self.gameLoop()
	
	def gameLoop(self):

		while True:
			# ensure we're running at a stable FPS
			self.clock.tick(FRAME_RATE)

			# handle user input
			self.handle_input()

			# update positions, handle collisions, etc
			self.g.update()

			# draw
			self.g.drawScreen()

	def handle_input(self):
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
			self.handle_keys(event)

	
	def handle_keys(self, event):
		'''
			Handle input from user keyboard
		'''
		if event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				sys.exit(1)
			return
			# move left
			if event.key == K_LEFT:
				self.player.setVel(Vector2(-1,0) * PLAYER_SPEED)
			# move right
			elif event.key == K_RIGHT:
				self.player.setVel(Vector2(1,0) * PLAYER_SPEED)

			# fire
			elif event.key == K_SPACE:
				self.fireTorpedo()

			# exit game
			elif event.key == K_ESCAPE:
				sys.exit(0)

		elif event.type == pygame.KEYUP:
			# if we released either the left or right arrow key, stop moving
			if event.key == K_LEFT or event.key == K_RIGHT:
				self.player.setVel(Vector2(0,0))

if __name__ == '__main__':
	g = Game()
