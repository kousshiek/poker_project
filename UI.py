import itertools
import random
import sys
import os
import pygame
from pygame.locals import *

SCREEN_X = 1130
SCREEN_Y = 609

bg="back.jpg"

IMAGE_WIDTH = 72
IMAGE_HEIGHT = 96

START_X = 50
START_Y = 50
            
pygame.init()
screen = pygame.display.set_mode((SCREEN_X,SCREEN_Y),0,16)
pygame.display.set_caption("PokerProject")
back=pygame.image.load(bg).convert()
screen = pygame.display.get_surface()
clock = pygame.time.Clock()
while True:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(back,(0,0))
    pygame.display.update()