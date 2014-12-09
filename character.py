import pygame
import sys

class character(pygame.sprite.Sprite):
    gravity = 6.28
    XVel = 0
    YVel = 0
    jumpVel = 10
    groundVel = 5
    sprintVel = 7
    left = False
    right = False
    isGrounded = True
    hasDouble = True
    sprinting = False
    def __init__(self, startPosX, startPosY):
        pygame.sprite.Sprite.__init__(self)
        self.posx = startPosX
        self.posy = startPosY
        self.width = 13
        self.height = 25

    def jump(self):
        if self.isGrounded:
            self.YVel = -self.jumpVel
            self.isGrounded = False
        self.isGrounded = False
#        elif self.hasDouble:
#            self.yVel = -self.jumpVel
#            self.hasDouble = False

    def walkLeft(self):
        self.XVel = -self.groundVel

    def sprintLeft(self):
        self.XVel = -self.sprintVel

    def walkRight(self):
        self.XVel = self.groundVel

    def sprintRight(self):
        self.XVel = self.sprintVel

    def stopMoving(self):
        self.XVel = 0

    def landed(self):
        self.isGrounded  = True
        self.hasDouble = True

    def render(self,collision,window):
        self.posx += self.XVel
        self.posy += self.YVel
        if self.posy > 200:
            self.posy += self.gravity
        print "x",self.XVel
        print "y", self.YVel
        self.posy += self.YVel
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,25,25)
        pygame.draw.rect(window,self.red,(self.posx,self.posy,self.width,self.height))
        pygame.draw.rect(window,self.black,(self.posx,self.posy,self.width,self.height))
