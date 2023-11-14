#classes.py
import pygame
from functions import *
#Button class for game buttons
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
        #draw the rectangle on the screen
        pygame.draw.rect(screen,self.clr,self.rect,self.w)
        #draw the text on the screen, with adjustments to center it
        screen.blit(self.button_text,(self.x+45,self.y+5))
        #always run the mouseMoved method
        self.mouseMoved()

# Game state class
class GameState : 
    def __init__(self, GameState) :
        self.GameState = GameState
        self.title_text = text('Pong Game',250,250,36,(255,255,255))
        self.play_button = Button(100,400,(255,0,255),'Play',200,50)
        self.instructions_button = Button(550,400,(0,255,0),'Instructions',200,50)
    
    def run(self, screen) :
        if self.GameState == 1 : 
            screen.fill((0,0,0))
            self.play_button.draw(screen)
            self.instructions_button.draw(screen)
            screen.blit(self.title_text,(300,100))
            
        # Game State for Play Button
        if self.GameState == 2 : 
            screen.fill((21, 230, 52))

        # Game State for iunstructions button
            
            
                  
    
    def changestate(self, num): 
        self.GameState = num

