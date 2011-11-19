# Configuration variables to be used by rest of game
import os
from pygame.locals import *

WIDTH = 1024
HEIGHT = 768
IS_FULLSCREEN = False
FRAME_RATE = 60
TILEX = 32
TILEY = 32

GAME_TITLE = "Hackathon!"

# up, down, left right
MOVEMENT_KEYS = [K_w, K_s, K_a, K_d]

GAME_IMAGES = "images"
GAME_SOUNDS = "sounds"
GAME_MAPS = "maps"

START_X = WIDTH / 2
START_Y = HEIGHT / 2

PLAYER_SPEED = 8

# Player up, down, left, right sprites
PLAYER_IMAGES = ["characterUp1.png", "characterDown1.png", "characterLeft1.png", "characterRight1.png"]
PLAYER_UP = PLAYER_IMAGES[0]
PLAYER_DOWN = PLAYER_IMAGES[1]
PLAYER_LEFT = PLAYER_IMAGES[2]
PLAYER_RIGHT = PLAYER_IMAGES[3]

START_MENU = "START"
PLAY = "PLAY"