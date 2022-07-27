import pygame
import os
from Constants import YELLOW, RED, WIDTH, HEIGHT, WHITE


class MainView:
    def __init__(self, win, red, yellow):
        self._window = win
        self._red = red
        self._yellow = yellow

        self._yellow_spaceship_image = pygame.transform.rotate(
            pygame.transform.scale(pygame.image.load(os.path.join("Assets", "spaceship.png")), (55, 40)), -90)
        self._red_spaceship_image = pygame.transform.rotate(
            pygame.transform.scale(pygame.image.load(os.path.join("Assets", "rocket.png")), (55, 40)), 90)

        self._friendly_fire_image = pygame.transform.rotate(
            pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bullet.png")), (15, 15)), -90)
        self._enemy_fire_image = pygame.transform.rotate(
            pygame.transform.scale(pygame.image.load(os.path.join("Assets", "missile.png")), (15, 15)), 90)

        self._background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bg.jpg")),
                                                  (WIDTH, HEIGHT))
        self._font = pygame.font.SysFont('comicsans', 40)
        self._winner_font = pygame.font.SysFont('comicsans', 100)

    def display(self):
        self._window.blit(self._background, (0, 0))
        self._window.blit(self._yellow_spaceship_image, (self._yellow.xPos, self._yellow.yPos))
        self._window.blit(self._red_spaceship_image, (self._red.xPos, self._red.yPos))

        red_health_text = self._font.render(f"Health: {self._red.health}", 1, WHITE)
        yellow_health_text = self._font.render(f"Health: {self._yellow.health}", 1, WHITE)

        self._window.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
        self._window.blit(yellow_health_text, (10, 10))

        border = pygame.Rect(900 // 2 - 5, 0, 10, 500)
        pygame.draw.rect(self._window, (0, 0, 0), border)

        for bullet in self._red.bullets:
            # pygame.draw.rect(self._window, RED, bullet.rect)
            self._window.blit(self._enemy_fire_image, (bullet.x, bullet.y + 2))
        for bullet in self._yellow.bullets:
            # pygame.draw.rect(self._window, YELLOW, bullet.rect)
            self._window.blit(self._friendly_fire_image, (bullet.x, bullet.y + 2))

        pygame.display.update()

    def show_winner(self, yellow_won):
        if yellow_won:
            text = "You Won!!"
        else:
            text = "You Lost!!"
        draw_text = self._winner_font.render(text, 1, WHITE)
        self._window.blit(draw_text, (WIDTH / 2 - draw_text.get_width() /
                                      2, HEIGHT / 2 - draw_text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(3000)

    def show_level(self, level):

        text = f"LEVEL {level}"
        draw_text = self._winner_font.render(text, 1, WHITE)
        self._window.blit(draw_text, (WIDTH / 2 - draw_text.get_width() /
                                      2, HEIGHT / 2 - draw_text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.display.update()
