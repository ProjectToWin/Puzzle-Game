import pygame, sys
from pygame.locals import *
from Board import Board
from Wall import Wall
from Player import Player
from Boulder import Boulder
from Key import Key

#WALL = pygame.image.load(os.path.join('sprite', 'wall.png'))

pygame.init()
#pygame.display.setCaption("The Game: Level 1")
screen = pygame.display.set_mode((320, 240))

clock = pygame.time.Clock()
walls = []
boulders = []
player = Player()
board = Board()
keys = []

level = [
"WWWWWWWWWWWWWWWWWWWW",
"WR                 W",
"W         WWWWWW   W",
"W   WWWW B     W   W",
"W   W        WWWW  W",
"W WWW  WWWW    B   W",
"W   W     W WW     W",
"W   W     W   WWW WW",
"W   WWW WWW   W W  W",
"W     W   W   W W  W",
"WWW   W   WWWWW W  W",
"W W      WW        W",
"W W   WWWW   WWW   W",
"W     W        W   W",
"WWWWWWWWWWWWWWWWWWWW",
]

board.placeWalls(level, walls)
board.placeBoulders(level, boulders)
board.placeKey(level, keys, "Red")

while True:
        
        clock.tick(60)

        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
                player.move(-2,0,walls,boulders)
        if key[pygame.K_RIGHT]:
                player.move(2,0,walls,boulders)
        if key[pygame.K_UP]:
                player.move(0,-2,walls,boulders)
        if key[pygame.K_DOWN]:
                player.move(0,2,walls,boulders)

        screen.fill((0,0,0))
        for wall in walls:
                pygame.draw.rect(screen,(255,255,255),wall.rect)
        for boulder in boulders:
                pygame.draw.rect(screen,(151,102,0),boulder.rect)
        for key in keys:
                pygame.draw.rect(screen, (255,0,0), key.rect)
        pygame.draw.rect(screen, (255, 200, 0), player.rect)
        pygame.display.flip()
