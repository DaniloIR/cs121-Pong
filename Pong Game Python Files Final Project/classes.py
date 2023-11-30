#classes.py
import pygame
import random
#ball class
class Ball:
    def __init__(self,x,y,clr,r):
        self.x=x
        self.y=y
        self.clr=clr
        self.r=r
        self.vel_x=5
        self.vel_y=5
        self.surf=pygame.surface.Surface((self.r,self.r))
    def update(self):
        self.x+=self.vel_x
        self.y+=self.vel_y
    #check edges method to check if the ball is off the screen, so the other player gets a point
    def checkEdges(self):
        if self.x>800:
            #give point to first player
            print('first player scores')
            self.x=400
            self.y=300
        if self.x<0:
            #give point to second player
            print('player 2 scores')
            self.x=400
            self.y=300
        if self.y>580:
            self.vel_y*=-1
        if self.y<0:
            self.vel_y*=-1
    def draw(self,screen):
        self.surf.fill(self.clr)
        self.update()
        self.checkEdges()
        screen.blit(self.surf,(self.x,self.y))
        #pygame.draw.circle(screen,self.clr,(self.x,self.y),self.r)
def text (txt,x,y,size,clr):
    #bring in screen variable
    screen = pygame.display.set_mode((800, 600))
    #font Variable, freesansbold font, size
    font=pygame.font.Font('freesansbold.ttf',size)
    #text variable, string, anti-aliasing true, color
    text=font.render(str(txt),True,clr)
    return text



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
        if self.y>=495:
            self.y=495
        if self.y<=0:
            self.y=0
    #check for collision with ball
    def checkColiding(self,ball):
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        rect=self.surf.get_rect()
        ball_rect=ball.surf.get_rect()
       # if ball.x>self.x and self.x+self.height
    def draw(self,screen,ball):   
        #always run checkEdges
        self.checkEdges()  
        self.checkColiding(ball)
        #blit the paddles to the screen
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        screen.blit(self.surf,(self.x,self.y)) 