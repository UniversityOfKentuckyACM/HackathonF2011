import math
import Actor
import util

from Vector2 import Vector2

from config import *

class Player(Actor.Actor):
	'''
		Player class. images is a list of images for each direction. We may need
		to alter this to support animation.
	'''
	def __init__(self,gameState):
		super(Player,self).__init__()
		
		# load all images
		# up, down, left, right
		self.images = [0] * 4
		self.images[0], self.rect = util.loadImage(PLAYER_IDLE_UP, -1)
		self.images[1], self.rect = util.loadImage(PLAYER_IDLE_DOWN, -1)
		self.images[2], self.rect = util.loadImage(PLAYER_IDLE_LEFT, -1)
		self.images[3], self.rect = util.loadImage(PLAYER_IDLE_RIGHT, -1)
		
		# 0 = up, 1 = down, 2 = left, 3 = right
		self.direction = 0
		
		# assign image and position
		self.setImage(self.images[self.direction])
		self.setPos(START_X, START_Y)

		self.gameState = gameState
	
	# Orient player with mouse
	def orient(self, mousePos):
		loc = mousePos - Vector2(self.getPos())
		angle = math.atan2(loc[1],loc[0])
		mag = math.fabs(angle)
		
		# if we're facing to the right
		if mag < math.pi / 4:
			self.setDir(3)
		# move left
		elif mag > 3*math.pi / 4:
			self.setDir(2)
		# either up or down
		else:
			if angle < 0:
				self.setDir(0)
			else:
				self.setDir(1)
	
	def setDir(self, newDir):
		self.direction = newDir
		self.image = self.images[self.direction]
	
	def move(self, m):
		'''
			Press a key and add to our velocity vector
		'''
		if m == -1:
			self.vel = Vector2(0,0)
		elif m == 0:
			self.vel += Vector2(0,-1) * PLAYER_SPEED
		elif m == 1:
			self.vel += Vector2(0,1) * PLAYER_SPEED
		elif m == 2:
			self.vel += Vector2(-1,0) * PLAYER_SPEED
		elif m == 3:
			self.vel += Vector2(1,0) * PLAYER_SPEED
	
	def unMove(self, m):
		'''
			Once a key is released, remove that from velocity vector.
		'''
		if m == 0:
			self.vel -= Vector2(0,-1) * PLAYER_SPEED
		elif m == 1:
			self.vel -= Vector2(0,1) * PLAYER_SPEED
		elif m == 2:
			self.vel -= Vector2(-1,0) * PLAYER_SPEED
		elif m == 3:
			self.vel -= Vector2(1,0) * PLAYER_SPEED
	
	# To do
	def swingSword(self):
		'''
			When mouse is pressed, sword is pushed out
		'''
		print "sword swung"
	
	
	# TODO
	def update(self):
		super(Player,self).update()

		# Check to see if we have touched edge of the screen
		if self.rect.left < TILEX * 2:
			self.gameState.nextMap("left", self.getPos())
		elif self.rect.right > WIDTH - (TILEX*2):
			self.gameState.nextMap("right", self.getPos())
		elif self.rect.top < 0:
			self.gameState.nextMap("up", self.getPos())
		elif self.rect.bottom > HEIGHT:
			self.gameState.nextMap("down", self.getPos())

