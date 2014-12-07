import pygame

CYAN = (0,255,234)
PURPLE = (255,0,255)
GREEN = (0,255,0)

class LevelFormat:
	def __init__(self, player, platforms, goal):
		self.player = player
		#self.switch = switch
		self.platforms = platforms
		self.goal = goal

class Player:
	def __init__(self, x, y, w, h):
		self.color = CYAN
		self.rect = pygame.Rect(x, y, w, h)
	def draw(self,surface):
		pygame.draw.rect(surface, self.color, self.rect)

#class Switch:
#	def __init__(self, x, y):
#		self.color = PURPLE
#		self.rect = pygame.Rect(x, y, 70, 70)
#		self.sets = None
#	def draw(self, surface):
#		pygame.draw.rect(surface, self.color, self.rect)

class Goal:
	def __init__(self, x, y):
		self.color = GREEN
		self.rect = pygame. Rect(x, y, 100, 100)
	def draw(self, surface):
		pygame.draw.rect(surface, self.color, self.rect)
