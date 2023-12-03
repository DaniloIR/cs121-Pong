##Functions.py
import pygame
#import the paddle, button, and ball classes
from paddle import *
from button import *
from ball import *
#import mixer so that sounds can be played
from pygame import mixer
pygame.init()
#load the sounds and music of the game
mixer.music.load('Pong Game Python Files Final Project/Assets/Sounds/main-menu-music.mp3')
beep_sound=mixer.Sound('Pong Game Python Files Final Project/Assets/Sounds/beep.wav')
game_over_sound=mixer.Sound('Pong Game Python Files Final Project/Assets/Sounds/game_over.wav')
win_sound=mixer.Sound('Pong Game Python Files Final Project/Assets/Sounds//win.wav')

#load the images of the game
background=pygame.image.load('Pong Game Python Files Final Project/Assets/Images/Main-Menu.jpg')
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
#Game state for main menu
def menu(screen,clock):
    #play the main menu music infinitely 
    mixer.music.play(-1)
    running= True
    #title text, play button and instructions button
    title_text=text('Pong Game',300,300,36,(250,250,250))
    play_button=Button(100,400,(255,0,255),'Play',200,50)
    instructions_button=Button(550,400,(0,255,0),'Instructions',200,50)
    #while loop for screen drawing

  
    while running==True:
        #fill the screen with a blue color, draw the buttons and text
        screen.blit(background,(0,0))
        play_button.draw(screen)
        instructions_button.draw(screen)
        screen.blit(title_text,(300,100))
        clock.tick(60)
        pygame.display.update()
        #button click events
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if play_button.mouseMoved():
                    #change the game state to game when play is pressed
                    mixer.music.stop()
                    #play a beep sound when the button is pressed
                    mixer.Sound.play(beep_sound)
                    return 'Game'
                if instructions_button.mouseMoved():
                    mixer.music.stop()
                    mixer.Sound.play(beep_sound)
                    return 'Instructions'    
            if event.type==pygame.QUIT:
                running=False
        pygame.display.flip()

#create 2 paddle objects
paddle1=Paddle(100,200,(255,0,0),10,100)
paddle2=Paddle(750,200,(0,255,0),10,100)
#create a ball object
ball=Ball(400,200,(255,255,255),20)
#game function for main game
#function for ball to check edges


def game(screen,clock):
    #create a font variable, so that the score can be updated every frame. Size of 32
    font=pygame.font.Font('freesansbold.ttf',32)
    paddle_collision(paddle1,ball)
    #player 1 and 2 scores as text to display
    running=True
    #the loop
    while running==True:
        #render the scores 
        player1_score_text=font.render('Player 1 Score:'+str(ball.player1_score),True,(255,255,255))
        player2_score_text=font.render('Player 2 Score:'+str(ball.player2_score),True,(255,255,255))
        #draw the ball, paddles, and score text
        screen.fill((0,0,0))
        ball.draw(screen)
        screen.blit(player1_score_text,(100,15))
        screen.blit(player2_score_text,(500,15))
        paddle1.draw(screen,ball)
        paddle2.draw(screen,ball)
        #get the key inputs and move the paddles accordingly
        if pygame.key.get_pressed()[pygame.K_w]:
                    paddle1.y-=15
        if pygame.key.get_pressed()[pygame.K_s]:
                    paddle1.y+=15
        if pygame.key.get_pressed()[pygame.K_o]:
                    paddle2.y-=15
        if pygame.key.get_pressed()[pygame.K_l]:
                    paddle2.y+=15
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        clock.tick(60)
        pygame.display.flip()
def paddle_collision(paddle,ball):
    paddle_surf=paddle.surf
    #paddlerect=paddle_surf.get_pos()


#instructions screen
def instructions (screen, clock) : 
    running=True
    home_button=Button(300,450,(0,255,0),'Home',150,50)
    rules_txt_1 = text(' RULES: ', 5, 10, 25, (255, 255, 255))
    rules_txt_2 = text(' 1: Each player gets 1 paddle on each side of the screen. ', 5, 10, 25, (255, 255, 255))
    rules_txt_3 = text(' This can be controlled with either the (W & S) or (O and L) keys ', 5, 10, 25, (255, 255, 255))
    rules_txt_4 = text(' 2: The object of the game is to keep the ball from hitting your  ', 5, 10, 25, (255, 255, 255))
    rules_txt_5 = text(' side of the screen before it hits the paddle; this will result in   ', 5, 10, 25, (255, 255, 255))
    rules_txt_6 = text(' a point for the other team   ', 5, 10, 25, (255, 255, 255))
    rules_txt_7 = text(' 3: The first player to get to a score of 21 wins!   ', 5, 10, 25, (255, 255, 255))
    rules_txt_8 = text(' 4: There will be power-ups and other fun challenges hidden   ', 5, 10, 25, (255, 255, 255))
    rules_txt_9 = text(' within the game so.. watch out!  ', 5, 10, 25, (255, 255, 255))
    rules_txt_10 = text(' Good Luck and Have Fun!!  ', 5, 10, 25, (255, 255, 255))
    while running ==True:
        screen.fill((0,0,0))
        home_button.draw(screen)
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
        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if home_button.mouseMoved():
                    mixer.Sound.play(beep_sound)
                    return 'Menu'
