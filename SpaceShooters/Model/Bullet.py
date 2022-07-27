from pygame.sprite import Sprite
import pygame


class Bullet:
    def __init__(self, x, y, friendly, level=0):
        self.x = x
        self.y = y
        self.height = 15
        self.width = 15
        self.friendly = friendly
        self.velocity = 7 + level - 1
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        if self.friendly:
            self.x += self.velocity
            self.rect.x += self.velocity
        else:
            self.x -= self.velocity
            self.rect.x -= self.velocity
