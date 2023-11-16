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
clock=pygame.time.Clock()
### Global Variables

# Create the screen
screen = pygame.display.set_mode((800, 600))
#Set window title
pygame.display.set_caption('Pong Game')
#running variable
running=True
#title text


game_state='Menu'
while running==True:
    if game_state=='Menu':
        game_state=menu(screen,clock)
        clock.tick(60)
    if game_state=='Game':
        game_state=game(screen,clock)
        clock.tick(60)
    if game_state=='Instructions':
        game_state=instructions(screen,clock)
        clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
#### The Loop
#while running:


        #event type for keyboard button press

        #added mousebuttondown event so the buttons register the click
        if event.type==pygame.MOUSEBUTTONDOWN:
            if GameState.play_button.mouseMoved()==True:
                GameState.changestate(2)
            if GameState.instructions_button.mouseMoved()==True:
                GameState.changestate(3)
                screen.fill((28, 17, 240))
                rules_txt_1 = text(' RULES: ', 5, 10, 25, (255, 255, 255))
                rules_txt_2 = text(' 1: Each player gets 1 paddle on each side of the screen. ', 5, 10, 25, (255, 255, 255))
                rules_txt_3 = text(' This can be controlled with either the (W & S) or (I and K) keys ', 5, 10, 25, (255, 255, 255))
                rules_txt_4 = text(' 2: The object of the game is to keep the ball from hitting your  ', 5, 10, 25, (255, 255, 255))
                rules_txt_5 = text(' side of the screen before it hits the paddle; this will result in   ', 5, 10, 25, (255, 255, 255))
                rules_txt_6 = text(' a point for the other team   ', 5, 10, 25, (255, 255, 255))
                rules_txt_7 = text(' 3: The first player to get to a score of 21 wins!   ', 5, 10, 25, (255, 255, 255))
                rules_txt_8 = text(' 4: There will be power-ups and other fun challenges hidden   ', 5, 10, 25, (255, 255, 255))
                rules_txt_9 = text(' within the game so.. watch out!  ', 5, 10, 25, (255, 255, 255))
                rules_txt_10 = text(' Good Luck and Have Fun!!  ', 5, 10, 25, (255, 255, 255))

                screen.blit(rules_txt_1, (350, 10) )
                screen.blit(rules_txt_2, (5, 50) )
                screen.blit(rules_txt_3, (5, 80) )
                screen.blit(rules_txt_4, (5, 110) )
                screen.blit(rules_txt_5, (5, 140) )
                screen.blit(rules_txt_6, (5, 170) )
                screen.blit(rules_txt_7, (5, 200) )
                screen.blit(rules_txt_8, (5, 230) )
                screen.blit(rules_txt_9, (5, 260) )
                screen.blit(rules_txt_10, (250, 310) )

        
                
                #2: The object of the game is to keep the ball from hitting your 

                #side of the screen before it hits the paddle; this will result in 

                #a point for the other team 3: The first player to get to a 
                #score of 21 wins! 
                #4: There will be power-ups and other fun challenges hidden within 
                #the game 5: Have Fun!
            

