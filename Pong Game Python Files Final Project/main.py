'''
##Title
Pong Game Final Project
#Authors
Danilo Reece (dir5@stmarys-ca.edu)
Joshua Press (jep14@stmarys-ca.edu)
Hector Gonzalez (hag10@stmarys-ca.edu)
Justin Sim (js109@stmarys-ca.edu)


##Software
Python 3.11.5
##
Required Modules:Pygame
https://www.pygame.org
Using version 2.5.2
'''
## Imports
import pygame
from classes import *
from functions import *
#initilize pygame
pygame.init()

### Global Variables

# Create the screen
screen = pygame.display.set_mode((800, 600))
#Set window title
pygame.display.set_caption('Pong Game')
#running variable
running=True
#title text
title_text=text('Pong Game',200,250,36,(255,255,255))

#### The Loop
while running:
    screen.fill((0,0,255))
    screen.blit(title_text,(250,200))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.update()