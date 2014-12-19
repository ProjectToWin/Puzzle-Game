import pygame
from Key import RedKey,BlueKey,GreenKey

class Player(object):

	def __init__(self):
		self.rect = pygame.Rect(32,32,16,16)
		self.bKey = False
		self.rKey = False
		self.gKey = False

	def move(self, moveX, moveY, walls, boulders):
		if moveX !=0:
			self.moveOneAxis(moveX,0,walls, boulders)
		if moveY !=0:
			self.moveOneAxis(0,moveY,walls, boulders)

	def moveOneAxis(self, moveX, moveY, walls, boulders):
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
					boulder.moveBoulder(moveX, moveY, walls, boulders)
				if moveX < 0:
					self.rect.left = boulder.rect.right
					boulder.rect.x += -1
					boulder.moveBoulder(moveX, moveY, walls, boulders)
				if moveY > 0:
					self.rect.bottom = boulder.rect.top
					boulder.rect.y += 1
					boulder.moveBoulder(moveX, moveY, walls, boulders)
				if moveY < 0:
					self.rect.top = boulder.rect.bottom
					boulder.rect.y += -1
					boulder.moveBoulder(moveX, moveY, walls, boulders)

#	def setBKey(self):
#		self.bKey = True

#	def setBKey(self):
#		self.bKey = True

#	def setBKey(self):
#		self.bKey = True
