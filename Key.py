import pygame

class RedKey(object):

	def __init__(self, pos, keys):
		keys.append(self)
		self.rect = pygame.Rect(pos[0],pos[1],16,16)
	def collideKey(self,player):
		if player.rect.colliderect(self.rect):
			player.setRKey()

class BlueKey(object)
	def __init__(self, pos, keys):
		keys.append(self)
		self.rect = pygame.Rect(pos[0],pos[1],16,16)
	def collideKey(self,player):
		if player.rect.colliderect(self.rect):
			player.setBKey

class GreenKey(object):
	def __init__(self, pos, keys):
		keys.append(self)
		self.rect = pygame.Rect(pos[0],pos[1],16,16)
	def collideKey(self,player):
		if player.rect.colliderect(self.rect):
			player.setGKey

class redDoor(object)
	def __init__(self, pos, doors):
		doors.append(self)
		self.rect = pygame.Rect(pos[0], pos[1], 16,16)