import pygame

class Boulder(object):

	def __init__(self, pos, boulders):
		boulders.append(self)
		self.rect = pygame.Rect(pos[0],pos[1],16,16)

	def moveBoulder(self, moveX, moveY, walls, boulders):
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