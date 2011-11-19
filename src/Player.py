
import Actor
import util

from Vector2 import Vector2

from config import *

class Player(Actor.Actor):
	'''
		Player class. images is a list of images for each direction. We may need
		to alter this to support animation.
	'''
	def __init__(self):
		super(Player,self).__init__()
		
		# load all images
		# up, down, left, right
		self.images = [0] * 4
		self.images[0], self.rect = util.loadImage(PLAYER_UP, -1)
		self.images[1], self.rect = util.loadImage(PLAYER_DOWN, -1)
		self.images[2], self.rect = util.loadImage(PLAYER_LEFT, -1)
		self.images[3], self.rect = util.loadImage(PLAYER_RIGHT, -1)
		
		# 0 = up, 1 = down, 2 = left, 3 = right
		self.direction = 0
		
		# assign image and position
		self.setImage(self.images[self.direction])
		self.setPos(START_X, START_Y)
	
	def setDir(self, newDir):
		self.direction = newDir
		self.setImage(self.images[self.direction])
	
	def move(self, m):
		if m == -1:
			self.vel = Vector2(0,0)
		elif m == 0:
			self.vel = Vector2(0,-1) * PLAYER_SPEED
		elif m == 1:
			self.vel = Vector2(0,1) * PLAYER_SPEED
		elif m == 2:
			self.vel = Vector2(-1,0) * PLAYER_SPEED
		elif m == 3:
			self.vel = Vector2(1,0) * PLAYER_SPEED
	
	# TODO
	def update(self):
		super(Player,self).update()

