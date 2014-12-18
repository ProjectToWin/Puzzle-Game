import pygame
from Wall import Wall
from Boulder import Boulder
from Key import Key

class Board(object):
	def __init__(self):
		print("")

	def placeWalls(self, level, walls):
		x = y = 0
		for row in level:
			for col in row:
				if col == "W":
					Wall((x,y),walls)
				x += 16
			x = 0
			y += 16

	def placeBoulders(self, level, boulders):
		x = y = 0
		for row in level:
			for col in row:
				if col == "B":
					Boulder((x,y), boulders)
				x += 16
			x = 0
			y += 16

	def placeKey(self, level, keys):
		x = y = 0
		for row in level:
			for col in row:
				if col == "R"-:
					Key((x,y), keys, color)
					
				x += 16
			x = 0
			y += 16