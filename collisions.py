import pygame
from Character import character
from Platform import Sprite

pygame.init()

window = pygame.display.set_mode((800,600))
 
pygame.display.set_caption("Collision Detection")

black = (0,0,0)
white = (255,255,255)
red = (255,25,25)
SCALE = 100
clock = pygame.time.Clock()

class myCollision:

    def detectCollisions(self,Sprite1,Sprite2):
        self.x1 = Sprite1.posx
        self.x2 = Sprite2.posx
        self.y1 = Sprite1.posy
        self.y2 = Sprite2.posy
        self.w1 = Sprite1.width
        self.w2 = Sprite2.width
        self.h1 = Sprite1.height
        self.h2 = Sprite2.height
        if self.x2+self.w2>=self.x1>=self.x2 and self.y2+self.h2>=self.y1>=self.y2:
            return True
        elif self.x2+self.w2>=self.x1+self.w1>=self.x2 and self.y2+self.h2>=self.y1>=self.y2:
            return True
        elif (self.x2+self.w2>=self.x1>=self.x2 and self.y2+self.h2>=self.y1+self.h1>=self.y2):
            return True
        elif (self.x2+self.w2>=self.x1+self.w1>=self.x2 and self.y2+self.h2>=self.y1+self.h1>=self.y2):
            return True
        else:
            return False

    def checkGrounded (self, Sprite1, Sprite2):
        c = myCollision()
        checkerSprite = Sprite(Sprite2.posx,Sprite2.posy,Sprite2.width,5)
        if c.detectCollisions(Sprite1, checkerSprite)is True:
            #blah
            Sprite1.isGrounded = True
