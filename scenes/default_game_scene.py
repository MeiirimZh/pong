import pygame

from scripts.player import Player
from scripts.ball import Ball


class DefaultGameScene:
    def __init__(self, game_state_manager, data, display):
        self.game_state_manager = game_state_manager
        self.data = data
        self.display = display

        self.screen_width = self.display.get_size()[0]
        self.screen_height = self.display.get_size()[1]

        self.player_1 = Player(20, 150, self.screen_height, 100, 7)
        self.player_2 = Player(20, 150, self.screen_height, 1160, 7)
        self.ball = Ball(30, 30, self.screen_width, self.screen_height, 10, 10, 1, 0)

    def run(self):
        self.render()
        self.update_players()

    def render(self):
        pygame.draw.rect(self.display, self.data.player_1_color, self.player_1.rect)
        pygame.draw.rect(self.display, self.data.player_2_color, self.player_2.rect)
        pygame.draw.rect(self.display, self.data.ball_color, self.ball.rect)

    def handle_player_1_input(self, keys):
        if keys[pygame.K_w]:
            self.player_1.y = self.change_y(self.player_1.y, self.player_1.height, -1, self.player_1.speed)
        if keys[pygame.K_s]:
            self.player_1.y = self.change_y(self.player_1.y, self.player_1.height, 1, self.player_1.speed)

    def handle_player_2_input(self, keys):
        if keys[pygame.K_UP]:
            self.player_2.y = self.change_y(self.player_2.y, self.player_2.height, -1, self.player_2.speed)
        if keys[pygame.K_DOWN]:
            self.player_2.y = self.change_y(self.player_2.y, self.player_2.height, 1, self.player_2.speed)

    def change_y(self, obj_y, obj_height, direction, speed):
        if direction == 1:
            return min(self.screen_height - obj_height, obj_y + speed)
        elif direction == -1:
            return max(0, obj_y - speed)
        elif direction == 0:
            pass
        else:
            raise TypeError("direction must be 1 or -1!")

    def update_players(self):
        self.player_1.rect.y = self.player_1.y
        self.player_2.rect.y = self.player_2.y

    def update_ball(self):
        pass
