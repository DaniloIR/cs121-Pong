##Functions.py
import pygame
#import the paddle, button, and ball classes
from paddle import *
from button import *
from ball import *
import random
#import mixer so that sounds can be played
from pygame import mixer





############# global variables
play_button=Button(100,400,(255,0,255),'Play',200,50)
paddle1=Paddle(75,200,(255,0,0),10,100,1)
paddle2=Paddle(750,200,(0,255,0),10,100,2)
ball=Ball(400,200,(255,255,255),20)
home_button=Button(300,450,(0,255,0),'Home',150,50)








######## background images
bg1=pygame.image.load('Assets/Images/bg1.png')
bg2=pygame.image.load('Assets/Images/bg2.jpg')
bg3=pygame.image.load('Assets/Images/bg3.jpg')
bg4=pygame.image.load('Assets/Images/bg4.jpg')
bg5=pygame.image.load('Assets/Images/bg5_lower_brightness.jpg')
bg6=pygame.image.load('Assets/Images/bg6_lower_brightness.jpg')
bg7=pygame.image.load('Assets/Images/bg7.jpg')
#function to reset background, returns a random background
def reset_background():
    background=[bg1,bg2,bg3,bg4,bg5,bg6,bg7]
    bg_num=random.randint(0,6)
    return background[bg_num]







pygame.init()
#load the sounds and music of the game
beep_sound=mixer.Sound('Assets/Sounds/beep.wav')
game_over_sound=mixer.Sound('Assets/Sounds/game_over.wav')
powerup_sound=mixer.Sound('Assets/Sounds/powerup.wav')
#load the images of the game
background=pygame.image.load('Assets/Images/Main-Menu.jpg')


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











###################Game state for main menu
def menu(screen,clock):
    #load the main menu song
    mixer.music.load('Assets/Sounds/game_song.wav')
    #play the main menu music infinitely 
    mixer.music.play(-1)
    #set running to true
    running= True
    #title text, play button and instructions button
    title_text=text('Pong Game',300,300,36,(250,250,250))
    instructions_button=Button(475,400,(0,255,0),'Instructions',200,50)
    #while loop for screen drawing

  
    while running==True:
        #fill the screen with the background, and draw buttons/text
        screen.blit(background,(0,0))
        play_button.draw(screen)
    
        instructions_button.draw(screen)
        screen.blit(title_text,(300,100))
        #update the display
        clock.tick(60)
        pygame.display.update()
        #button click events
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if play_button.mouseMoved():
                    #run the resetgame function
                    resetGame()
                    #change the game state to game when play is pressed
                    mixer.music.stop()
                    #play a beep sound when the button is pressed
                    mixer.Sound.play(beep_sound)
                    #unload the music so that the ending music will work
                    mixer.music.unload()
                    #change state to instructions
                    return 'Game'
                if instructions_button.mouseMoved():
                    #stop the music
                    mixer.music.stop()
                    #play a sound
                    mixer.Sound.play(beep_sound)
                    #unload the music
                    mixer.music.unload()
                    return 'Instructions'    
            if event.type==pygame.QUIT:
                running=False
        pygame.display.flip()












#############resetgame function to reset the positions of the paddle, ball, and player scores

def resetGame():
    #set player 1 and 2 score to 0
    ball.player1_score=0
    ball.player2_score=0
    #reset the locations and heights of the paddles
    paddle1.y=200
    paddle2.y=200
    paddle1.height=100
    paddle2.height=100
    #reset the ball location
    ball.x=400
    ball.y=200
    #set the score intervals back so that powerups work again
    ball.not_reached_5_paddle_1=True
    ball.not_reached_5_paddle_2=True
    ball.not_reached_8_paddle_1=True
    ball.not_reached_8_paddle_2=True












##################### game function
def game(screen,clock):
    #get a new random background
    random_background=reset_background()
    #create a font variable, so that the score can be updated every frame. Size of 32
    font=pygame.font.Font('freesansbold.ttf',32)
    running=True
    #the loop
    while running==True:
        #blit the background to the screen
        screen.blit(random_background,(0,0))
        #render the scores 
        player1_score_text=font.render('Player 1 Score:'+str(ball.player1_score),True,(255,255,255))
        player2_score_text=font.render('Player 2 Score:'+str(ball.player2_score),True,(255,255,255))
        #look for collisions between ball and paddle
        paddle_collision()
        #draw the bal
        ball.draw(screen)
        #blit the score text to the screen
        screen.blit(player1_score_text,(100,15))
        screen.blit(player2_score_text,(500,15))
        #draw the paddles to the screen
        paddle1.draw(screen,ball)
        paddle2.draw(screen,ball)
        #get the key inputs and move the paddles accordingly
        if pygame.key.get_pressed()[pygame.K_w]:
                    paddle1.y-=8
        if pygame.key.get_pressed()[pygame.K_s]:
                    paddle1.y+=8
        if pygame.key.get_pressed()[pygame.K_o]:
                    paddle2.y-=8
        if pygame.key.get_pressed()[pygame.K_l]:
                    paddle2.y+=8
        #if the escape key is pressed, go to the menu
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    return 'Menu'
        #quit the game
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        #update the screen
        clock.tick(60)
        pygame.display.flip()
        #run the update_paddle function (for powerups)
        adjust_paddle(ball.player1_score,ball.player2_score)
        #if the score of either player is 10, go to the game over screen and play a sound
        if ball.player1_score==10 or ball.player2_score==10:
            return 'Game Over'
      







############# #paddle collision function to use with ball
def paddle_collision():
    #if the first paddle is colliding with the ball
    if paddle1.checkColiding(ball)=='collision paddle 1':
        #make the ball move faster
       ball.vel_x=10
       ball.vel_y=10
       #if the second paddle is colliding with the ball
    if paddle2.checkColiding(ball)=='collision paddle 2':
        #make the ball faster
        ball.vel_x=-10
        ball.vel_y=-10












############adjust different parts of the paddle when a score is reached, take in the scores
def adjust_paddle(p1_score,p2_score):
    #if the score of the first player is 5 and has not reached 5 already
    if p1_score ==5 and ball.not_reached_5_paddle_1:
        #make the paddle bigger and play a sound
        paddle1.height=250
        mixer.Sound.play(powerup_sound,1)
        #set the variable to false so the sound won't play forever
        ball.not_reached_5_paddle_1 = False
    #if the score of the second player is 5 and has not reached 5 already
    if p2_score ==5 and ball.not_reached_5_paddle_2:
        #make the paddle bigger and play a sound
        paddle2.height=250
        mixer.Sound.play(powerup_sound,1)
        #set the variable to false so the sound won't play forever
        ball.not_reached_5_paddle_2 = False
    #if the score of the first player is 8 and has not reached 8 already
    if p1_score ==8 and ball.not_reached_8_paddle_1:
        #make the paddle smaller and play a sound
        paddle1.height=25
        mixer.Sound.play(powerup_sound,1)
        ball.not_reached_8_paddle_1 = False
    #if the score of the second player is 8 and has not reached 8 already
    if p2_score ==8 and ball.not_reached_8_paddle_2:
        #make the paddle smaller and play a sound
        paddle2.height=25
        mixer.Sound.play(powerup_sound,1)
        #set the variable to false so the sound won't play forever
        ball.not_reached_8_paddle_2 = False













###################instructions screen
def instructions (screen, clock) : 
    #move the home button back to it's original location
    home_button=Button(300,450,(0,255,0),'Home',150,50)
    running=True
    # rules text variables
    rules_txt_1 = text(' RULES: ', 5, 10, 25, (255, 255, 255))
    rules_txt_2 = text(' 1: Each player gets 1 paddle on each side of the screen. ', 5, 10, 25, (255, 255, 255))
    rules_txt_3 = text(' This can be controlled with either the (W & S) or (O and L) keys ', 5, 10, 25, (255, 255, 255))
    rules_txt_4 = text(' 2: The object of the game is to keep the ball from hitting your  ', 5, 10, 25, (255, 255, 255))
    rules_txt_5 = text(' side of the screen before it hits the paddle; this will result in   ', 5, 10, 25, (255, 255, 255))
    rules_txt_6 = text(' a point for the other team   ', 5, 10, 25, (255, 255, 255))
    rules_txt_7 = text(' 3: The first player to get to a score of 10 wins!   ', 5, 10, 25, (255, 255, 255))
    rules_txt_8 = text(' 4: There will be power-ups and other fun challenges hidden   ', 5, 10, 25, (255, 255, 255))
    rules_txt_9 = text(' within the game so.. watch out!  ', 5, 10, 25, (255, 255, 255))
    rules_txt_10 = text(' Good Luck and Have Fun!!  ', 5, 10, 25, (255, 255, 255))
    rules_txt_11=text('Press escape in the game to go to the main menu',5,10,25,(255,255,255))
    while running ==True:
        #game loop for instructions
        screen.fill((0,0,0))
        #draw the button and each of the text for the rules
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
        screen.blit(rules_txt_11,(5,360))
        pygame.display.update()
        clock.tick(60)
        #update the game and get button presses
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if home_button.mouseMoved():
                    mixer.Sound.play(beep_sound)
                    return 'Menu'











####################game over screen
def game_over(screen,clock):
    #load the game ending music
    mixer.music.load('Assets/Sounds/Halo.wav')
    mixer.music.play(-1)
    #move the home button location
    home_button=Button(475,400,(0,255,0),'Home',150,50)
    running=True
    #make a variable called winner.
    winner=0
    #determine who won by checking the values of the scores
    if ball.player1_score>ball.player2_score:
        winner=1
    else:
        winner=2
    #make text to display who the winner is
    winner_text=text(f'Player {winner} won the game!',200,200,32,(255,255,255))
    game_over_text=text('GAME OVER',200,50,64,(255,255,255))
    while running==True:
        
        #fill the screen with a red color
        screen.fill((255,0,0))
        #draw the text and buttons on the screen
        home_button.draw(screen)
        screen.blit(game_over_text,(200,50))
        screen.blit(winner_text,(200,200))
        play_button.draw(screen)
        pygame.display.update()
        clock.tick(60)
        #get button clicks
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if home_button.mouseMoved():
                    mixer.Sound.play(beep_sound)
                    #unload the music so that the main menu music can play again
                    mixer.music.unload()
                    return 'Menu'
                if play_button.mouseMoved():
                    mixer.Sound.play(beep_sound)
                    resetGame()
                    mixer.music.unload()
                    return 'Game'
            if event.type==pygame.QUIT:
                running=False
