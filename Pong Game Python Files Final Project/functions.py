##Functions.py
import pygame
from classes import *
import pygame

#ball class
class Ball:
    def __init__(self,x,y,clr,r):
        self.x=x
        self.y=y
        self.clr=clr
        self.r=r
    def draw(self,screen):
        pygame.draw.circle(screen,self.clr,(self.x,self.y),self.r)
#button class for clicking and mouse moved
class Button:
    #init method with x,y,color,text,width,height. A rectangle uses pygame.rect, and text uses the text function
    def __init__(self,x,y,clr,txt,w,h):
        self.x=x
        self.y=y
        self.clr=clr
        self.w=w
        self.h=h
        self.txt=txt
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
        self.button_text=text(str(self.txt),self.x,self.y,25,(255,255,255))
        self.surf=pygame.surface.Surface((self.w,self.h))
    #mouseMoved method to check for a collision with the mouse
    def mouseMoved(self):
        #get the mouse's position
        mouse=pygame.mouse.get_pos()
        #iscolliding checks if the mouse is colliding with the button
        iscolliding=self.rect.collidepoint(mouse)
        if iscolliding==True:
            #change the color of the button and return true (this is so that the button can be clicked)
            self.clr=(255,255,0)
            return True
        #change the button's color once the mouse moves off of the button
        else:
            self.clr=(255,0,255)
    #draw method for the main loop. screen is taken in so the button and text can be drawn
    def draw(self,screen):
        self.surf.fill(self.clr)
        #draw the rectangle on the screen
        screen.blit(self.surf,(self.x,self.y))
        #draw the text on the screen, with adjustments to center it
        screen.blit(self.button_text,(self.x+45,self.y+5))
        #always run the mouseMoved method
        self.mouseMoved()

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
    running= True
    #title text, play button and instructions button
    title_text=text('Pong Game',300,300,36,(250,250,250))
    play_button=Button(100,400,(255,0,255),'Play',200,50)
    instructions_button=Button(550,400,(0,255,0),'Instructions',200,50)
    #while loop for screen drawing
    while running==True:
        #fill the screen with a blue color, draw the buttons and text
        screen.fill((0,0,0))
        play_button.draw(screen)
        instructions_button.draw(screen)
        screen.blit(title_text,(300,100))
        clock.tick(60)
        pygame.display.update()
        #button click events
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if play_button.mouseMoved():
                    return 'Game'
                if instructions_button.mouseMoved():
                    return 'Instructions'
            if event.type==pygame.QUIT:
                running=False
        pygame.display.flip()
#paddle class for game
class Paddle:
    def __init__(self,x,y,clr,width,height):
        self.x=x
        self.y=y
        self.clr=clr
        self.width=width
        self.height=height
        self.surf=pygame.surface.Surface((self.width,self.height))
        self.surf.fill(self.clr)
    def checkEdges(self):
        #checkedges method to make sure that paddles don't go off screen
        if self.y>=500:
            self.y=500
        if self.y<=0:
            self.y=0
    def draw(self,screen):   
        #always run checkEdges
        self.checkEdges()  
        #blit the paddles to the screen
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        screen.blit(self.surf,(self.x,self.y)) 
#create 2 paddle objects
paddle1=Paddle(100,200,(255,0,0),10,100)
paddle2=Paddle(750,200,(0,255,0),10,100)
#player 1 and 2 scores
player1_score=0
player2_score=0
#create a ball object
ball=Ball(400,200,(255,255,255),20)
#game function for main game
def game(screen,clock):
    #player 1 and 2 scores as text to display
    player1_score_text=text('Player 1 Score:'+str(player1_score),0,15,32,(255,255,255))
    player2_score_text=text('Player 2 Score:'+str(player2_score),450,15,32,(255,255,255))
    running=True
    #the loop
    while running==True:
        #draw the ball, paddles, and score text
        screen.fill((0,0,0))
        ball.draw(screen)
        screen.blit(player1_score_text,(100,15))
        screen.blit(player2_score_text,(500,15))
        paddle1.draw(screen)
        paddle2.draw(screen)
        
        #get the key inputs and move the paddles accordingly
        if pygame.key.get_pressed()[pygame.K_w]:
                    paddle1.y+=15
        if pygame.key.get_pressed()[pygame.K_s]:
                    paddle1.y-=15
        if pygame.key.get_pressed()[pygame.K_o]:
                    paddle2.y+=15
        if pygame.key.get_pressed()[pygame.K_l]:
                    paddle2.y-=15
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        clock.tick(60)
        pygame.display.flip()
    
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
                    return 'Menu'
