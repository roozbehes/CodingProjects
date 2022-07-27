from Model.Bullet import Bullet
from Constants import MAX_BULLETS
import pygame

from Constants import WIDTH , HEIGHT


class Yellow:
    def __init__(self):
        self.health = 10
        self.xPos = 300
        self.yPos = 100
        self.velocity = 5
        self.width = 55
        self.height = 40
        self.bullets = []
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)

    def move_left(self):
        if self.xPos - self.velocity > 0:
            self.xPos -= self.velocity
            self.rect.x -= self.velocity

    def move_right(self):
        if self.xPos + self.velocity + self.width < 445:
            self.xPos += self.velocity
            self.rect.x += self.velocity

    def move_up(self):
        if self.yPos - self.velocity > 0:
            self.yPos -= self.velocity
            self.rect.y -= self.velocity

    def move_down(self):
        if self.yPos + self.velocity + self.height + 15 < 500:
            self.yPos += self.velocity
            self.rect.y += self.velocity

    def shoot(self):
        if len(self.bullets) <= MAX_BULLETS:
            bullet = Bullet(self.xPos + self.width, self.yPos + self.height / 2 - 2 , True)
            self.bullets.append(bullet)

    def update_bullets(self, red_player):
        for bullet in self.bullets:
            bullet.move()
            if red_player.rect.colliderect(bullet.rect):
                pygame.event.post(pygame.event.Event(pygame.USEREVENT+2))
                self.bullets.remove(bullet)
            elif bullet.x > WIDTH:
                self.bullets.remove(bullet)
