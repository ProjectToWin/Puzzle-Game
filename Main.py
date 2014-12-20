#Adventure Cubed

import pygame, sys, os
from pygame.locals import *

class Player(object):

        def __init__(self, pos):
                self.rect = pygame.Rect(pos[0],pos[1],16,16)

        def move(self, moveX, moveY):
                if moveX !=0:
                        self.moveOneAxis(moveX,0)
                if moveY !=0:
                        self.moveOneAxis(0,moveY)

        def moveOneAxis(self, moveX, moveY):
                self.rect.x += moveX
                self.rect.y += moveY
                
                for wall in walls:
                        if self.rect.colliderect(wall.rect):
                                if moveX > 0:
                                        self.rect.right = wall.rect.left
                                if moveX < 0:
                                        self.rect.left = wall.rect.right
                                if moveY > 0:
                                        self.rect.bottom = wall.rect.top
                                if moveY < 0:
                                        self.rect.top = wall.rect.bottom
                for boulder in boulders:
                        if self.rect.colliderect(boulder.rect):
                                if moveX > 0:
                                        self.rect.right = boulder.rect.left
                                        boulder.rect.x += 1
                                        boulder.moveBoulder(moveX, moveY)
                                if moveX < 0:
                                        self.rect.left = boulder.rect.right
                                        boulder.rect.x += -1
                                        boulder.moveBoulder(moveX, moveY)
                                if moveY > 0:
                                        self.rect.bottom = boulder.rect.top
                                        boulder.rect.y += 1
                                        boulder.moveBoulder(moveX, moveY)
                                if moveY < 0:
                                        self.rect.top = boulder.rect.bottom
                                        boulder.rect.y += -1
                                        boulder.moveBoulder(moveX, moveY)


class Wall(object):

        def __init__(self, pos):
                walls.append(self)
                self.rect = pygame.Rect(pos[0],pos[1],16,16)

class Boulder(object):

        def __init__(self, pos):
                boulders.append(self)
                self.rect = pygame.Rect(pos[0],pos[1],16,16)

        def moveBoulder(self, moveX, moveY):
                for wall in walls:
                        if self.rect.colliderect(wall.rect):
                                if moveX > 0:
                                        self.rect.right = wall.rect.left
                                if moveX < 0:
                                        self.rect.left = wall.rect.right
                                if moveY > 0:
                                        self.rect.bottom = wall.rect.top
                                if moveY < 0:
                                        self.rect.top = wall.rect.bottom
                for boulder in boulders:
                        if self.rect.colliderect(boulder.rect) and boulder.rect != self.rect:
                                if moveX > 0:
                                        self.rect.right = boulder.rect.left
                                if moveX < 0:
                                        self.rect.left = boulder.rect.right
                                if moveY > 0:
                                        self.rect.bottom = boulder.rect.top
                                if moveY < 0:
                                        self.rect.top = boulder.rect.bottom


class Game():
        def __init__(self):
                self.gameState = 1

        def makeLevel(self):

                if self.gameState == 1:
                        rKey = False
                        gKey = False
                        bKey = False
                        yButton = False
                        yOn = False
                        oButton = False
                        oOn = False
                        pButton = False
                        pOn = False
                        level = [
                        "WWWWWWWWWW",
                        "WCB  W E W",
                        "WWW  W   W",
                        "W     BBBW",
                        "W        W",
                        "WWWWWWWWWW"]

                if self.gameState == 2:
                        rKey = False
                        gKey = False
                        bKey = False
                        yButton = False
                        yOn = False
                        oButton = True
                        oOn = True
                        pButton = False
                        pOn = False
                        level = [
                        'WWWWWWWWWWWW',
                        'WWW        W',
                        'WWW        W',
                        'WWW        W',
                        'WC         W',
                        'WWW    WWBWW',
                        'WWW    W  WW',
                        'WWW    W  WW',
                        'WWW    W  WW',
                        'WWW    W  WW',
                        'WWW    WWOWW',
                        'WWW    oWEWW',
                        'WWWWWWWWWWWW']

                if self.gameState == 3:
                        rKey = False
                        gKey = False
                        bKey = True
                        yButton = False
                        yOn = False
                        oButton = True
                        oOn = True
                        pButton = False
                        pOn = False
                        level = [
                        "WWWWWWWWWWWW",
                        "WWWCB  WoWWW",
                        "WE BW BK WWW",
                        "WWWO  B    W",
                        "WWWWWWWWWkWW",
                        "WWWWWWWWWWWW"]

                if self.gameState == 4:
                        rKey = False
                        gKey = False
                        bKey = True
                        yButton = False
                        yOn = False
                        oButton = True
                        oOn = True
                        pButton = False
                        pOn = False
                        level = [
                        'WWWWWWWWWWWWWWWW',
                        'WW WWWWWWW   WWW',
                        'WkB        W WWW',
                        'WWOW W W W   KEW',
                        'WW   WBW W W WWW',
                        'WWWW C Wo    WWW',
                        'WWWWWWWWWWWWWWWW']

                if self.gameState == 5:
                        rKey = True
                        gKey = False
                        bKey = True
                        yButton = True
                        yOn = True
                        oButton = True
                        oOn = True
                        pButton = True
                        pOn = True
                        level = [
                        'WWWWWWWWWWWWWWWW',
                        'WWWWWWoWWWWWWWWW',
                        'WWWWWWPWWWWWWWWW',
                        'W   pW      O  W',
                        'W C WW BWW WWEWW',
                        'W    WB  WkWWWWW',
                        'WWBW W   WrWWWWW',
                        'WWyWY    K WWWWW',
                        'WWRWW WWWWWWWWWW',
                        'WW    WWWWWWWWWW',
                        'WWWWWWWWWWWWWWWW']
                        
                screen = pygame.display.set_mode((len(level[0])*16, len(level)*16))
                x = y = 0
                wallsize = len(walls)
                increment = 0
                """print wallsize
                if wallsize !=0:
                        while(increment<wallsize):
                                walls.pop(increment)  
                                increment +=1
                                print(increment)"""
                walls[:]=[]
                boulders[:] = []
                for boulder in boulders:
                        del boulder

                for row in level:
                        for col in row:
                                if col == "C":
                                        player = Player((x,y))
                                if col == "W":
                                        Wall((x,y))
                                if col == "B":
                                        hitBoulder = Boulder((x,y))
                                if col == "r":
                                        redKey = pygame.Rect(x,y,16,16)
                                if col == "R":
                                        redDoor = pygame.Rect(x,y,16,16)
                                if col == "g":
                                        greenKey = pygame.Rect(x,y,16,16)
                                if col == "G":
                                        greenDoor = pygame.Rect(x,y,16,16)
                                if col == "k":
                                        blueKey = pygame.Rect(x,y,16,16)
                                if col == "K":
                                        blueDoor = pygame.Rect(x,y,16,16)
                                if col == "y":
                                        yellowButton = pygame.Rect(x,y,16,16)
                                if col == "Y":
                                        yellowDoor = pygame.Rect(x,y,16,16)
                                if col == "o":
                                        orangeButton = pygame.Rect(x,y,16,16)
                                if col == "O":
                                        orangeDoor = pygame.Rect(x,y,16,16)
                                if col == "p":
                                        purpleButton = pygame.Rect(x,y,16,16)
                                if col == "P":
                                        purpleDoor = pygame.Rect(x,y,16,16)
                                if col == "E":
                                        exit = pygame.Rect(x,y,16,16)
                                x += 16
                        x = 0
                        y += 16
                while True:

                        clock.tick(60)

                        for event in pygame.event.get():
                                if event.type == QUIT:
                                        pygame.quit()
                                        sys.exit()
                        key = pygame.key.get_pressed()
                        if key[pygame.K_LEFT]:
                                player.move(-2,0)
                                horizontal = 2
                        if key[pygame.K_RIGHT]:
                                player.move(2,0)
                                horizontal = -2
                        if key[pygame.K_UP]:
                                player.move(0,-2)
                                vertical = -2
                        if key[pygame.K_DOWN]:
                                player.move(0,2)
                                vertical = 2
                        else:
                                vrtical = 0
                                horizontal = 0

                        screen.fill((0,0,0))
                        if player.rect.colliderect(exit):
                                self.gameState+=1
                                self.makeLevel()
                        for wall in walls:
                                screen.blit(WALL,wall.rect)
                        for boulder in boulders:       
                                if rKey:
                                        screen.blit(RK,redKey)
                                        screen.blit(RD,redDoor)
                                        if player.rect.colliderect(redKey):
                                                rKey = False
                                        if boulder.rect.colliderect(redKey):
                                                if horizontal > 0:
                                                        boulder.rect.right = redKey.left
                                                if horizontal < 0:
                                                        boulder.rect.left = redKey.right
                                                if vertical > 0:
                                                        boulder.rect.bottom = redKey.top
                                                if vertical < 0:
                                                        boulder.rect.top = redKey.bottom
                                        if player.rect.colliderect(redDoor):
                                                if horizontal > 0:
                                                        player.rect.right = redDoor.left
                                                if horizontal < 0:
                                                        player.rect.left = redDoor.right
                                                if vertical > 0:
                                                        player.rect.bottom = redDoor.top
                                                if vertical < 0:
                                                        player.rect.top = redDoor.bottom
                                        if boulder.rect.colliderect(redDoor):
                                                if horizontal > 0:
                                                        boulder.rect.right = redDoor.left
                                                if horizontal < 0:
                                                        boulder.rect.left = redDoor.right
                                                if vertical > 0:
                                                        boulder.rect.bottom = redDoor.top
                                                if vertical < 0:
                                                        boulder.rect.top = redDoor.bottom
                                if gKey:
                                        screen.blit(GK,greenKey)
                                        screen.blit(GD,greenDoor)
                                        if player.rect.colliderect(greenKey):
                                                gKey = False
                                        if boulder.rect.colliderect(greenKey):
                                                if horizontal > 0:
                                                        boulder.rect.right = greenKey.left
                                                if horizontal < 0:
                                                        boulder.rect.left = greenKey.right
                                                if vertical > 0:
                                                        boulder.rect.bottom = greenKey.top
                                                if vertical < 0:
                                                        boulder.rect.top = greenKey.bottom
                                        if player.rect.colliderect(greenDoor):
                                                if horizontal > 0:
                                                        player.rect.right = greenDoor.left
                                                if horizontal < 0:
                                                        player.rect.left = greenDoor.right
                                                if vertical > 0:
                                                        player.rect.bottom = greenDoor.top
                                                if vertical < 0:
                                                        player.rect.top = greenDoor.bottom
                                        if boulder.rect.colliderect(greenDoor):
                                                if horizontal > 0:
                                                        boulder.rect.right = greenDoor.left
                                                if horizontal < 0:
                                                        boulder.rect.left = greenDoor.right
                                                if vertical > 0:
                                                        boulder.rect.bottom = greenDoor.top
                                                if vertical < 0:
                                                        boulder.rect.top = greenDoor.bottom
                                if bKey:
                                        screen.blit(BK,blueKey)
                                        screen.blit(BD, blueDoor)
                                        if player.rect.colliderect(blueKey):
                                                bKey = False
                                        if boulder.rect.colliderect(blueKey):
                                                if horizontal > 0:
                                                        boulder.rect.right = blueKey.left
                                                if horizontal < 0:
                                                        boulder.rect.left = blueKey.right
                                                if vertical > 0:
                                                        boulder.rect.bottom = blueKey.top
                                                if vertical < 0:
                                                        boulder.rect.top = blueKey.bottom
                                        if player.rect.colliderect(blueDoor):
                                                if horizontal > 0:
                                                        player.rect.right = blueDoor.left
                                                if horizontal < 0:
                                                        player.rect.left = blueDoor.right
                                                if vertical > 0:
                                                        player.rect.bottom = blueDoor.top
                                                if vertical < 0:
                                                        player.rect.top = blueDoor.bottom
                                        if boulder.rect.colliderect(blueDoor):
                                                if horizontal > 0:
                                                        boulder.rect.right = blueDoor.left
                                                if horizontal < 0:
                                                        boulder.rect.left = blueDoor.right
                                                if vertical > 0:
                                                        boulder.rect.bottom = blueDoor.top
                                                if vertical < 0:
                                                        boulder.rect.top = blueDoor.bottom
                                if yOn:
                                        screen.blit(YB,yellowButton)
                                        if yButton:
                                                screen.blit(YD,yellowDoor)
                                                if player.rect.colliderect(yellowButton):
                                                        yButton = False
                                                if boulder.rect.colliderect(yellowButton):
                                                        yButton = False
                                                        hitBoulder = boulder
                                                if player.rect.colliderect(yellowDoor):
                                                        if horizontal > 0:
                                                                player.rect.right = yellowDoor.left
                                                        if horizontal < 0:
                                                                player.rect.left = yellowDoor.right
                                                        if vertical > 0:
                                                                player.rect.bottom = yellowDoor.top
                                                        if vertical < 0:
                                                                player.rect.top = yellowDoor.bottom
                                                if boulder.rect.colliderect(yellowDoor):
                                                        if horizontal > 0:
                                                                boulder.rect.right = yellowDoor.left
                                                        if horizontal < 0:
                                                                boulder.rect.left = yellowDoor.right
                                                        if vertical > 0:
                                                                boulder.rect.bottom = yellowDoor.top
                                                        if vertical < 0:
                                                                boulder.rect.top = yellowDoor.bottom
                                        elif player.rect.colliderect(yellowButton): 
                                                yButton = False
                                        elif hitBoulder.rect.colliderect(yellowButton):
                                                yButton = False
                                        else:
                                                yButton = True
                                if oOn:
                                        screen.blit(OB,orangeButton)
                                        if oButton:
                                                screen.blit(OD,orangeDoor)
                                                if player.rect.colliderect(orangeButton):
                                                        oButton = False
                                                if boulder.rect.colliderect(orangeButton):
                                                        oButton = False
                                                        hitBoulder = boulder
                                                if player.rect.colliderect(orangeDoor):
                                                        if horizontal > 0:
                                                                player.rect.right = orangeDoor.left
                                                        if horizontal < 0:
                                                                player.rect.left = orangeDoor.right
                                                        if vertical > 0:
                                                                player.rect.bottom = orangeDoor.top
                                                        if vertical < 0:
                                                                player.rect.top = orangeDoor.bottom
                                                if boulder.rect.colliderect(orangeDoor):
                                                        if horizontal > 0:
                                                                boulder.rect.right = orangeDoor.left
                                                        if horizontal < 0:
                                                                boulder.rect.left = orangeDoor.right
                                                        if vertical > 0:
                                                                boulder.rect.bottom = orangeDoor.top
                                                        if vertical < 0:
                                                                boulder.rect.top = orangeDoor.bottom
                                        elif player.rect.colliderect(orangeButton): 
                                                oButton = False
                                        elif hitBoulder.rect.colliderect(orangeButton):
                                                oButton = False
                                        else:
                                                oButton = True
                                if pOn:
                                        screen.blit(PB,purpleButton)
                                        if pButton:
                                                screen.blit(PD,purpleDoor)
                                                if player.rect.colliderect(purpleButton):
                                                        pButton = False
                                                if boulder.rect.colliderect(purpleButton):
                                                        pButton = False
                                                        hitBoulder = boulder
                                                if player.rect.colliderect(purpleDoor):
                                                        if horizontal > 0:
                                                                player.rect.right = purpleDoor.left
                                                        if horizontal < 0:
                                                                player.rect.left = purpleDoor.right
                                                        if vertical > 0:
                                                                player.rect.bottom = purpleDoor.top
                                                        if vertical < 0:
                                                                player.rect.top = purpleDoor.bottom
                                                if boulder.rect.colliderect(purpleDoor):
                                                        if horizontal > 0:
                                                                boulder.rect.right = purpleDoor.left
                                                        if horizontal < 0:
                                                                boulder.rect.left = purpleDoor.right
                                                        if vertical > 0:
                                                                boulder.rect.bottom = purpleDoor.top
                                                        if vertical < 0:
                                                                boulder.rect.top = purpleDoor.bottom
                                        elif player.rect.colliderect(purpleButton): 
                                                pButton = False
                                        elif hitBoulder.rect.colliderect(purpleButton):
                                                pButton = False
                                        else:
                                                pButton = True
                        screen.blit(EXIT,exit)
                        for boulder in boulders:
                                screen.blit(BOULDER,boulder.rect)
                        screen.blit(PLAYER,player.rect)
                        pygame.display.flip()


pygame.init()


WALL = pygame.image.load('sprite/wall.png')
PLAYER = pygame.image.load('sprite/player.png')
BOULDER = pygame.image.load('sprite/boulder.png')
RK = pygame.image.load('sprite/redkey.png')
RD = pygame.image.load('sprite/reddoor.png')
GK = pygame.image.load('sprite/greenkey.png')
GD = pygame.image.load('sprite/greendoor.png')
BK = pygame.image.load('sprite/bluekey.png')
BD = pygame.image.load('sprite/bluedoor.png')
YB = pygame.image.load('sprite/yellowbutton.png')
YD = pygame.image.load('sprite/yellowdoor.png')
OB = pygame.image.load('sprite/orangebutton.png')
OD = pygame.image.load('sprite/orangedoor.png')
PB = pygame.image.load('sprite/purplebutton.png')
PD = pygame.image.load('sprite/purpledoor.png')
EXIT = pygame.image.load('sprite/exit.png')

clock = pygame.time.Clock()
game = Game()

walls = []
boulders = []

global player
global hitBoulder
global screen

global rKey
global gKey
global bKey
global yButton
global yOn
global oButton
global oOn
global pButton
global pOn

vertical = 0
horizontal = 0

game.makeLevel()






