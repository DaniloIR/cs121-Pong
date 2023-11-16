##Functions.py
import pygame
from classes import *
import pygame
'''
#Text function to make displaying text simpler. 
 Arguments are text, x location, 
 y location, size, and color
'''
def text (txt,x,y,size,clr):
    #bring in screen variable
    screen = pygame.display.set_mode((800, 600))
    #font Variable, freesansbold font, size
    font=pygame.font.Font('freesansbold.ttf',size)
    #text variable, string, anti-aliasing true, color
    text=font.render(str(txt),True,clr)
    return text









def instructions (screen, clock) : 
    while running:
        GameState.run(screen)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
     
        if event.type==pygame.MOUSEBUTTONDOWN:
            if GameState.play_button.mouseMoved()==True:
                GameState.changestate(2)
            if GameState.instructions_button.mouseMoved()==True:
                GameState.changestate(3)
                screen.fill((28, 17, 240))
                rules_txt_1 = text(' RULES: ', 5, 10, 25, (255, 255, 255))
                rules_txt_2 = text(' RULES: 1: Each player gets 1 paddle on each side of the screen. ', 5, 10, 25, (255, 255, 255))
                rules_txt_3 = text(' This can be controlled with either the (W & S) or (I and K) keys ', 5, 10, 25, (255, 255, 255))
                rules_txt_4 = text(' 2: The object of the game is to keep the ball from hitting your  ', 5, 10, 25, (255, 255, 255))
                screen.blit(rules_txt_1, (200, 10) )
                screen.blit(rules_txt_2, (5, 40) )
                screen.blit(rules_txt_3, (5, 70) )
                screen.blit(rules_txt_4, (5, 100) )
