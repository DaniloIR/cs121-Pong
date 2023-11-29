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
        self.surf=pygame.surface.Surface((self.w,self.h))
        self.surf.fill(self.clr)
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
        screen.blit(self.surf,(self.x,self.y))
        #draw the text on the screen, with adjustments to center it
        screen.blit(self.button_text,(self.x+45,self.y+5))
        #always run the mouseMoved method
        self.mouseMoved()

class Paddle:
    def __init__(self,x,y,size,clr,width,height):
        self.x=x
        self.y=y
        self.size=size
        self.clr=clr
        self.width=width
        self.height=height
        self.surf=pygame.surface.Surface((self.width,self.height))
    
    def draw(self,screen):     
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        screen.blit(self.surf,(self.x,self.y))
        checkEdges()
