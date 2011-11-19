import pygame

import util
import sys
import math

from config import *

class TerrainLayer(pygame.Surface):
	'''
		This builds a map background
	'''
	def __init__(self):
		#make a surface
		#load the images
		#blit onto that shit.
		#pygame.Surface.__init__((WIDTH, HEIGHT))
		super(TerrainLayer,self).__init__((WIDTH,HEIGHT))
		#define a sub rect 
		grass,tmp = util.loadImage("grass.png")
		tile = pygame.Surface((TILEX,TILEY))
		tile.blit(grass, tmp)
		#self.blit(tile,(WIDTH/2,HEIGHT/2))
		#blit every other tile.
		for y in range(HEIGHT/TILEY):
			for x in range(WIDTH/TILEX):
				self.blit(tile, (x*TILEX, y*TILEY))
