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
GameState = GameState(1)
title_text=text('Pong Game',250,250,36,(0,0,0))
title_text=text('Pong Game',250,250,36,(250,250,250))
play_button=Button(100,400,(255,0,255),'Play',200,50)
instructions_button=Button(550,400,(0,255,0),'Instructions',200,50)
#### The Loop
while running:
    GameState.run(screen)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        #added mousebuttondown event so the buttons register the click
        if event.type==pygame.MOUSEBUTTONDOWN:
            if GameState.play_button.mouseMoved()==True:
                GameState.changestate(2)
            if GameState.instructions_button.mouseMoved()==True:
                GameState.changestate(3)
    pygame.display.update()

