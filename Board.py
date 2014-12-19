import pygame
from Wall import Wall
from Boulder import Boulder
from Key import RedKey, BlueKey, GreenKey


class Board(object):
    def __init__(self):
        print("")

    def placeWalls(self, level, walls):
        x = y = 0
        for row in level:
            for col in row:
                if col == "W":
                    Wall((x, y), walls)
                x += 16
            x = 0
            y += 16

    def placeBoulders(self, level, boulders):
        x = y = 0
        for row in level:
            for col in row:
                if col == "B":
                    Boulder((x, y), boulders)
                x += 16
            x = 0
            y += 16

    def placeRedKey(self, level, keys):
        x = y = 0
        for row in level:
            for col in row:
                if col == "r":
                    RedKey((x, y), keys)
                x += 16
            x = 0
            y += 16

    def placeBlueKey(self, level, keys):
        x = y = 0
        for row in level:
            for col in row:
                if col == "k":
                    BlueKey((x, y), keys)
                x += 16
            x = 0
            y += 16

    def placeGreenKey(self, level, keys):
        x = y = 0
        for row in level:
            for col in row:
                if col == "g":
                    GreenKey((x, y), keys)
                x += 16
            x = 0
            y += 16

    def placeRedDoor(self, level, doors):
        x = y = 0
        for row in level:
            for col in row:
                if col == "R":
                    GreenKey((x, y), doors)
                x += 16
            x = 0
            y += 16

    def placeBlueDoor(self, level, doors):
        x = y = 0
        for row in level:
            for col in row:
                if col == "K":
                    GreenKey((x, y), doors)
                x += 16
            x = 0
            y += 16

    def placeGreenDoor(self, level, doors):
        x = y = 0
        for row in level:
            for col in row:
                if col == "R":
                    GreenKey((x, y), doors)
                x += 16
            x = 0
            y += 16
