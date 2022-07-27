import random
from Model.Bullet import Bullet
from Constants import ENEMY_MAX_BULLETS
import pygame


class Red:
    def __init__(self , level):
        self.level = level
        self.health = 10 + level - 1
        self.xPos = 700
        self.yPos = 100
        self.velocity = 4 + level - 1
        self.width = 55
        self.height = 40
        self.move_count = 0
        self.rand_v = 0
        self.rand_h = 0
        self.rand_s = 0
        self.bullets = []
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)

    def move_left(self):
        if self.xPos - self.velocity > 455:
            self.xPos -= self.velocity
            self.rect.x -= self.velocity

    def move_right(self):
        if self.xPos + self.velocity + self.width < 900:
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

    def play(self):
        if self.move_count == 0:
            self.rand_v = random.randint(1, 10)
            self.rand_h = random.randint(1, 10)

        rand_shoot = random.randint(1, 10)
        self.move_count = (self.move_count + 1) % 10
        if self.rand_v >= 6:
            self.move_down()
        else:
            self.move_up()

        if self.rand_h >= 6:
            self.move_right()
        else:
            self.move_left()
        if self.move_count ==5:
            if rand_shoot >= 6:
                self.shoot()

    def shoot(self):
        if len(self.bullets) <= ENEMY_MAX_BULLETS + self.level - 1:
            bullet = Bullet(self.xPos, self.yPos + self.height // 2 - 2, False, self.level)
            self.bullets.append(bullet)

    def update_bullets(self, yellow_player):
        for bullet in self.bullets:
            bullet.move()
            if yellow_player.rect.colliderect(bullet.rect):
                pygame.event.post(pygame.event.Event(pygame.USEREVENT + 1))
                self.bullets.remove(bullet)
            elif bullet.x < 0:
                self.bullets.remove(bullet)
