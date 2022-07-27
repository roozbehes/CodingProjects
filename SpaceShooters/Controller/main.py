import pygame
from View.main import MainView
from Model.Red import Red
from Model.Yellow import Yellow
from Constants import WIDTH, HEIGHT


class MainController:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self._win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("SpaceShooter MVC")
        self._player_name = "Mohammad"
        self._level = 1
        self._red = Red(self._level)
        self._yellow = Yellow()
        self._view = MainView(self._win, self._red, self._yellow)
        self._clock = pygame.time.Clock()
        self.yellow_hit = pygame.USEREVENT + 1
        self.red_hit = pygame.USEREVENT + 2

    def handle_player_movement(self, key_pressed):
        if key_pressed[pygame.K_a]:
            self._yellow.move_left()
        if key_pressed[pygame.K_w]:
            self._yellow.move_up()
        if key_pressed[pygame.K_s]:
            self._yellow.move_down()
        if key_pressed[pygame.K_d]:
            self._yellow.move_right()
        self._view.display()

    def handle_random_player(self):
        self._red.play()

    def handle_bullets(self):
        self._yellow.update_bullets(self._red)
        self._red.update_bullets(self._yellow)

    def start_level(self):
        self._red = Red(self._level)
        self._yellow = Yellow()
        self._view.show_level(self._level)
        self._view = MainView(self._win, self._red, self._yellow)

    def run(self):
        running = True
        while running:
            self._clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self._yellow.shoot()
                if event.type == self.yellow_hit:
                    self._yellow.health -= 1
                if event.type == self.red_hit:
                    self._red.health -= 1
            key_pressed = pygame.key.get_pressed()
            self.handle_player_movement(key_pressed)
            self.handle_random_player()
            self.handle_bullets()
            if self._yellow.health == 0:
                #Player Loses
                self._view.show_winner(False)
                self.save_results()
                self._level = 1
                self.start_level()
            elif self._red.health == 0:
                #Go to Next Level
                self._level += 1
                self.start_level()

    def save_results(self):
        with open("results.csv", 'a') as file:
            file.write(f'\n{self._player_name},{self._level}')
        return
