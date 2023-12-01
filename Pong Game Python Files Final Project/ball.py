import pygame
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
            #print('first player scores')
            self.x=400
            self.y=300
            return 'player 1 scores'
        if self.x<0:
            #give point to second player
           # print('player 2 scores')
            self.x=400
            self.y=300
            return 'player 2 scores'
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