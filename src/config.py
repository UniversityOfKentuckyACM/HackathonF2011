# Configuration variables to be used by rest of game
import os
from pygame.locals import *

WIDTH = 1024
HEIGHT = 768
IS_FULLSCREEN = False
FRAME_RATE = 60

GAME_TITLE = "Hackathon!"

# up, down, left right
DIRECTION_KEYS = [K_w, K_s, K_a, K_d]

GAME_IMAGES = "images"
GAME_SOUNDS = "sounds"

#BACKGROUND_IMAGE = "sea.png"

START_X = WIDTH / 2
START_Y = HEIGHT / 2
PLAYER_SPEED = 4
PLAYER_IMAGES = ["characterUp.png", "characterDown.png", "characterLeft.png", "characterRight.png"]

START_MENU = "START"
PLAY = "PLAY"

#SUB_IMAGE = "sub.png"
#TORPEDO_IMAGE = "ship_fire.png"
#TORPEDO_VEL = (0,3)
#SUB_VEL = (2,0)

#ENEMY_SPAWN_INTERVAL = 60
