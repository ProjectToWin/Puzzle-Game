import pygame, sys, os
from pygame.locals import *

class Player(object):

        def __init__(self):
                self.rect = pygame.Rect(32,32,16,16)

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


pygame.init()
#pygame.display.setCaption("The Game: Level 1")
screen = pygame.display.set_mode((320, 240))

WALL = pygame.image.load(os.path.join('sprite', 'wall.png'))

clock = pygame.time.Clock()
walls = []
boulders = []
player = Player()

rKey = False
gKey = False
bKey = False
yButton = True
oButton = False
pButton = False
vertical = 0
horizontal = 0

level = [
"WWWWWWWWWWWWWWWWWWWW",
"W                  W",
"W         WWWWWW  yW",
"W   WWWW B     W   W",
"W   W        WWWW  W",
"W WWW  WWWW    B   W",
"W   W     W WW     W",
"W   W     W   WWWYWW",
"W   WWW WWW   W W  W",
"W     W   W   W W  W",
"WWW   W   WWWWW W  W",
"W W      WW        W",
"W W   WWWW   WWW   W",
"W     W        W   W",
"WWWWWWWWWWWWWWWWWWWW",
]

x = y = 0
for row in level:
        for col in row:
                if col == "W":
                        Wall((x,y))
                if col == "B":
                        Boulder((x,y))
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
                horizontal = 1
        if key[pygame.K_RIGHT]:
                player.move(2,0)
                horizontal = -1
        if key[pygame.K_UP]:
                player.move(0,-2)
                vertical = -1
        if key[pygame.K_DOWN]:
                player.move(0,2)
                vertical = 1
        else:
                vrtical = 0
                horizontal = 0

        screen.fill((0,0,0))
        for wall in walls:
                pygame.draw.rect(screen,(255,255,255),wall.rect)
                wall.rect.blit(WALL,(0,0))
        for boulder in boulders:
                pygame.draw.rect(screen,(151,102,0),boulder.rect)
        if rKey:
                pygame.draw.rect(screen,(255,0,0),redKey)
                pygame.draw.rect(screen,(255,0,0), redDoor)
                if player.rect.colliderect(redKey):
                        rKey = False
                if player.rect.colliderect(redDoor):
                        if horizontal > 0:
                                player.rect.right = redDoor.left
                        if horizontal < 0:
                                player.rect.left = redDoor.right
                        if vertical > 0:
                                player.rect.bottom = redDoor.top
                        if vertical < 0:
                                player.rect.top = redDoor.bottom
        if gKey:
                pygame.draw.rect(screen,(0,255,0),greenKey)
                pygame.draw.rect(screen,(0,255,0), greenDoor)
                if player.rect.colliderect(greenKey):
                        gKey = False
                if player.rect.colliderect(greenDoor):
                        if horizontal > 0:
                                player.rect.right = greenDoor.left
                        if horizontal < 0:
                                player.rect.left = greenDoor.right
                        if vertical > 0:
                                player.rect.bottom = greenDoor.top
                        if vertical < 0:
                                player.rect.top = greenDoor.bottom
        if bKey:
                pygame.draw.rect(screen,(0,0,255),blueKey)
                pygame.draw.rect(screen,(0,0,255), blueDoor)
                if player.rect.colliderect(blueKey):
                        bKey = False
                if player.rect.colliderect(blueDoor):
                        if horizontal > 0:
                                player.rect.right = blueDoor.left
                        if horizontal < 0:
                                player.rect.left = blueDoor.right
                        if vertical > 0:
                                player.rect.bottom = blueDoor.top
                        if vertical < 0:
                                player.rect.top = blueDoor.bottom
        pygame.draw.rect(screen,(200,200,200),yellowButton)
        if yButton:
                pygame.draw.rect(screen,(0,0,255), yellowDoor)
                if player.rect.colliderect(yellowButton):
                        yButton = False
                if player.rect.colliderect(yellowDoor):
                        if horizontal > 0:
                                player.rect.right = yellowDoor.left
                        if horizontal < 0:
                                player.rect.left = yellowDoor.right
                        if vertical > 0:
                                player.rect.bottom = yellowDoor.top
                        if vertical < 0:
                                player.rect.top = yellowDoor.bottom
        elif player.rect.colliderect(yellowButton):
                yButton = False
        else:
                yButton = True
        pygame.draw.rect(screen, (255, 200, 0), player.rect)
        pygame.display.flip()
