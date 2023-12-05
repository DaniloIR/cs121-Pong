#paddle class
import pygame

class Paddle:
    def __init__(self,x,y,clr,width,height,id):
        self.x=x
        self.y=y
        self.clr=clr
        self.width=width
        self.height=height
        self.surf=pygame.surface.Surface((self.width,self.height))
        self.surf.fill(self.clr)
        self.id=id
    def checkEdges(self):
        #checkedges method to make sure that paddles don't go off screen
        if self.y>=495:
            self.y=495
        if self.y<=0:
            self.y=0
    #check for collision with ball
    def checkColiding(self,ball):
        #the first id is the left paddle, the second is the right
        if self.id==1:
            #if the ball's y combined with the radius are greater 
            # than the first paddle's y as well and on the right side of the paddle, return a collision
            if ball.y+ball.r>self.y and ball.y-ball.r<self.y+self.height:
                if ball.x-ball.r<=self.x+self.width:
                    return 'collision paddle 1'
        elif self.id==2:
            #if the ball's y combined with the radius are greater 
            #than the second paddle's y as well and on the left side of the paddle, return a collision
            if ball.y+ball.r>self.y and ball.y-ball.r<self.y+self.height:
                if ball.x+ball.r>=self.x:
                    return 'collision paddle 2'
        else:
            return 'not colliding'
       # if ball.x>self.x and self.x+self.height
    def draw(self,screen,ball):   
        #always run checkEdges
        self.checkEdges()  
        self.checkColiding(ball)
        #blit the paddles to the screen
        self.surf=pygame.surface.Surface((self.width,self.height))
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        self.surf.fill(self.clr)
        screen.blit(self.surf,(self.x,self.y)) 