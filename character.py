import pygame
import sys

class character(pygame.sprite.Sprite):
    gravity = .1
    XVel = 0
    YVel = 0
    jumpVel = 5
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
        elif self.hasDouble:
            self.YVel = -self.jumpVel
            self.hasDouble = False

    def inAir(self):
        if self.isGrounded == False:
            self.YVel += self.gravity

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
        self.YVel = 0

    def render(self,collision,window):
        self.posx += self.XVel
        self.posy += self.YVel
        self.inAir()
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,25,25)
        pygame.draw.rect(window,self.red,(self.posx,self.posy,self.width,self.height))
        pygame.draw.rect(window,self.black,(self.posx,self.posy,self.width,self.height))
