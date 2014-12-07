import pygame
import sys

class character(pygame.sprite.Sprite)
    grvaity = 6.28
    XVel = 0
    Yvel = 0
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

    def jump(self):
        if self.isGrounded:
            yVel = jumpVel
            isGrounded = False
        elif self.hasDouble:
            yVel = jumpVel
            hasDouble = False   

    def walkLeft():
        self.XVel = -groundVel

    def sprintLeft():
        self.XVel = -sprintVel

    def walkRight():
        self.XVel = -groundVel

    def sprintRight():
        self.XVel = -sprintVel

    def stopMoving():
        self.XVel = 0
