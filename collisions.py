import pygame
 
pygame.init()
 
window = pygame.display.set_mode((800,600))
 
pygame.display.set_caption("Collision Detection")
 
black = (0,0,0)
white = (255,255,255)
red = (255,25,25)
SCALE = 100
clock = pygame.time.Clock()

dickNigga = False

 
def detectCollisions(Sprite1,Sprite2):

    x1 = Sprite1.x
    x2 = Sprite2.x
    y1 = Sprite1.y
    y2 = Sprite2.y
    w1 = Sprite1.width
    w2 = Sprite2.width
    h1 = Sprite1.height
    h2 = Sprite2.height
    if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
        #print("d")
        return True
    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
        #print("c")
        return True
    elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
        #print("b")
        return True
    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
        #print("a")
        return True
    else:
        return False

def checkGrounded (Sprite1, Sprite2):
    checkerSprite = Sprite(Sprite2.x,Sprite2.y,Sprite2.width,5)
    if detectCollisions(Sprite1, checkerSprite)is True:
        print "YES"
 
class Sprite:
 
    def __init__(self,x,y,width,height):
 
        self.x=x
 
        self.y=y
 
        self.width=width
 
        self.height=height
 
    def render(self,collision):
        if (collision==True):
            pygame.draw.rect(window,red,(self.x,self.y,self.width,self.height))
        else:
            pygame.draw.rect(window,black,(self.x,self.y,self.width,self.height))
#                     w  h
Sprite1=Sprite(100,50,50,50) #CHARACTER
Sprite2=Sprite(300,50,100,100)
 
moveX,moveY=0,0
 
gameLoop=True
while gameLoop:
 
    for event in pygame.event.get():
 
        if (event.type==pygame.QUIT):
 
            gameLoop=False
 
        if (event.type==pygame.KEYDOWN):
 
            if (event.key==pygame.K_LEFT):
 
                moveX = -4
 
            if (event.key==pygame.K_RIGHT):
 
                moveX = 4
 
            if (event.key==pygame.K_UP):
 
                moveY = -4
 
            if (event.key==pygame.K_DOWN):
 
                moveY = 4
 
        if (event.type==pygame.KEYUP):
 
            if (event.key==pygame.K_LEFT):
 
                moveX=0
 
            if (event.key==pygame.K_RIGHT):
 
                moveX=0
 
            if (event.key==pygame.K_UP):
 
                moveY=0
 
            if (event.key==pygame.K_DOWN):
 
                moveY=0
    window.fill(white)
    Sprite1.x+=moveX
    Sprite1.y+=moveY
    collisions=detectCollisions(Sprite1,Sprite2)
    checkGrounded(Sprite1,Sprite2)
    Sprite1.render(collisions)
    Sprite2.render(False)
    pygame.display.flip()

    clock.tick(50)

pygame.quit()
