import pygame


class RedKey(object):
    def __init__(self, pos, keys):
        keys.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

    def collideKey(self, player):
        if player.rect.colliderect(self.rect):
            player.rKey = True

class BlueKey(object):
    def __init__(self, pos, keys):
        keys.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

    def collideKey(self, player):
        if player.rect.colliderect(self.rect):
            player.bKey = True

class GreenKey(object):
    def __init__(self, pos, keys):
        keys.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

    def collideKey(self, player):
        if player.rect.colliderect(self.rect):
            player.gKey = True

class RedDoor(object):
    def __init__(self, pos, doors):
        doors.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
    def collideDoor(self, player):
        if player.rect.colliderect(self.rect):
            player.rKey = False

class BlueDoor(object):
    def __init__(self, pos, doors):
        doors.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
    def collideDoor(self, player):
        if player.rect.colliderect(self.rect):
            player.bKey = False

class GreenDoor(object):
    def __init__(self, pos, doors):
        doors.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
    def collideDoor(self, player):
        if player.rect.colliderect(self.rect):
            player.gKey = False
