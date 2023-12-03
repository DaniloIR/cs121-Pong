import pygame
#ball class
class Ball:
    #init method, x, y, color, radius values are passed in
    def __init__(self,x,y,clr,r):
        self.x=x
        self.y=y
        self.clr=clr
        self.r=r
        self.vel_x=5
        self.vel_y=5
        #surface, player 1 and 2 scores are 0 by default
        self.surf=pygame.surface.Surface((self.r,self.r))
        self.player1_score=0
        self.player2_score=0
    def update(self):
        self.x+=self.vel_x
        self.y+=self.vel_y
    #check edges method to check if the ball is off the screen, so the other player gets a point
    def checkEdges(self):
        if self.x>800:
            #give point to first player
            self.x=400
            self.y=300
            self.player1_score+=1
        if self.x<0:
            #give point to second player
            self.x=400
            self.y=300
            self.player2_score+=1
        if self.y>580:
            self.vel_y*=-1
        if self.y<0:
            self.vel_y*=-1
    def draw(self,screen):
        #fill the ball with the color, draw it, and run the other methods
        self.surf.fill(self.clr)
        self.update()
        self.checkEdges()
        screen.blit(self.surf,(self.x,self.y))