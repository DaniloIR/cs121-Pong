#paddle class
import pygame

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