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
from functions import *
#initilize pygame
pygame.init()
clock=pygame.time.Clock()
### Global Variables

# Create the screen
screen = pygame.display.set_mode((800, 600))
#Set window title
pygame.display.set_caption('Pong Game')
#load the game's icon and set it
icon=pygame.image.load('Assets/Images/Icon.png')
pygame.display.set_icon(icon)
#running variable
running=True
#title text
#set game state to menu by default
game_state='Menu'
######### the loop
while running==True:
    #window.blit(screen,(0,0))
    if game_state=='Menu':
        game_state=menu(screen,clock)
        clock.tick(60)
    if game_state=='Game':
        game_state=game(screen,clock)
        clock.tick(60)
    if game_state=='Instructions':
        game_state=instructions(screen,clock)
        clock.tick(60)
    if game_state=='Game Over':
        game_state=game_over(screen,clock)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
            

