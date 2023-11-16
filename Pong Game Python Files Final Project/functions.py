##Functions.py
import pygame
from classes import *
import pygame
'''
#Text function to make displaying text simpler. 
 Arguments are text, x location, 
 y location, size, and color
'''
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
def text (txt,x,y,size,clr):
    #bring in screen variable
    screen = pygame.display.set_mode((800, 600))
    #font Variable, freesansbold font, size
    font=pygame.font.Font('freesansbold.ttf',size)
    #text variable, string, anti-aliasing true, color
    text=font.render(str(txt),True,clr)
    return text


def menu(screen,clock):
    running= True
    title_text=text('Pong Game',250,250,36,(0,0,0))
    title_text=text('Pong Game',250,250,36,(250,250,250))
    play_button=Button(100,400,(255,0,255),'Play',200,50)
    instructions_button=Button(550,400,(0,255,0),'Instructions',200,50)
    while running==True:
        screen.fill((0,0,255))
        play_button.draw(screen)
        instructions_button.draw(screen)
        screen.blit(title_text,(300,100))
        clock.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if play_button.mouseMoved():
                    return 'Game'
                if instructions_button.mouseMoved():
                    return 'Instructions'
                
            if event.type==pygame.QUIT:
                running=False
   
    #return 'Menu'
def game(screen,clock):
    running=True
    while running==True:
        screen.fill((0,0,0))
        clock.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
def instructions(screen,clock):
    running=True
    while running==True:
        screen.fill((255,0,0))
        clock.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

