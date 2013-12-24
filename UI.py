#import itertools
#import random
import sys
#import os
import pygame
from pygame.locals import *

posx=[550,655,550,360,170,60,170]
posy=[300,165,25,25,25,165,300]
pot_posx=[586,640,586,396,206,160,206]
pot_posy=[290,213,131,131,131,213,290]
money_posx=[586,765,586,396,206,40,206]
money_posy=[406,213,15,15,15,213,406]
ingame=[1,1,1,1,1,1,1]
money_in_pot=[50,50,50,50,30,30,30]
remaining_money=[1200,1100,840,3080,600,200,700]
player_cards1=["images/Ac","images/2c","images/Ah","images/5s","images/Jc","images/front","images/Qd"]
player_cards2=["images/7d","images/8s","images/6s","images/Th","images/Td","images/front","images/7h"]

SCREEN_X = 795
SCREEN_Y = 511

bg="images/back.jpg"
hand_cards=["images/7c","images/5h"]
com_cards=["images/Js","images/7s","images/Th","images/front","images/front"]

IMAGE_WIDTH = 72
IMAGE_HEIGHT = 96

START_X = 50
START_Y = 50
            
pygame.init()
screen = pygame.display.set_mode((SCREEN_X,SCREEN_Y),0,32)
pygame.display.set_caption("PokerProject")
back=pygame.image.load(bg).convert()
hc_images=[pygame.image.load(hand_cards[0]).convert(),pygame.image.load(hand_cards[1]).convert()]
cc_image=[]
for i in range(0,5):
    cc_image.append(pygame.image.load(com_cards[i]).convert())
card1_image=[]
card2_image=[]
for i in range(0,7):
    card1_image.append(pygame.image.load(player_cards1[i]).convert())
    card2_image.append(pygame.image.load(player_cards2[i]).convert())
screen = pygame.display.get_surface()
clock = pygame.time.Clock()
#hand_cards=[]
while True:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(back,(0,0))
    screen.blit(hc_images[0],(320,300))
    screen.blit(hc_images[1],(320+72,300))
    for i in range(0,5):
        screen.blit(cc_image[i],(i*72+225,50+96+20))
    for i in range(0,7):
        if(ingame[i]):
            screen.blit(card1_image[i],(posx[i],posy[i]))
            screen.blit(card2_image[i],(posx[i]+15,posy[i]))
    for i in range(0,7):
        if(ingame[i]):
            font = pygame.font.Font(None, 24)
            rem_money_text = font.render("$"+str(remaining_money[i]), 1, (0, 255, 0))
            bet_money_text = font.render("$"+str(money_in_pot[i]), 1, (255,0, 0))
            rem_money_textpos = rem_money_text.get_rect()
            bet_money_textpos = bet_money_text.get_rect()
            rem_money_textpos.centerx=money_posx[i]
            bet_money_textpos.centerx=pot_posx[i]
            rem_money_textpos.centery=money_posy[i]
            bet_money_textpos.centery=pot_posy[i]
            screen.blit(rem_money_text, rem_money_textpos)
            screen.blit(bet_money_text, bet_money_textpos)
    pygame.display.update()
