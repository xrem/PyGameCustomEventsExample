import pygame
from os import path

WIDTH = 1024
HEIGHT = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (195, 195, 195)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

FPS = 30
BLOCK_WIDTH = 30

PLAYER_IMG_PATH = path.join(path.dirname(__file__), "player.png")
BLOCK_IMG_PATH = path.join(path.dirname(__file__), "block.png")
ADDBLOCK = pygame.USEREVENT + 1

STATE_IDLE = 0

STATE_UP = -1
STATE_DOWN = 1

STATE_LEFT = -1
STATE_RIGHT = 1