import pygame

from random import choice
from scripts.player import Player
from scripts.ball import Ball


class DefaultGameScene:
    def __init__(self, game_state_manager, data, display):
        self.game_state_manager = game_state_manager
        self.data = data
        self.display = display

        self.screen_width = self.display.get_size()[0]
        self.screen_height = self.display.get_size()[1]

        self.player_height = 150
        self.player_1 = Player(20, self.player_height, self.screen_height, 100, 7)
        self.player_2 = Player(20, self.player_height, self.screen_height, 1160, 7)
        self.ball = Ball(30, 30, self.screen_width, self.screen_height, 10, 10, 1, 0)

    def run(self):
        self.render()
        self.update_players()
        self.update_ball()
        self.detect_ball_collision()
        self.detect_goal()

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

    def change_x(self, obj_x, obj_width, direction, speed):
        if direction == 1:
            return min(self.screen_width - obj_width, obj_x + speed)
        elif direction == -1:
            return max(0, obj_x - speed)
        elif direction == 0:
            return obj_x
        else:
            raise TypeError("direction must be 1, (-1) or 0!")

    def change_y(self, obj_y, obj_height, direction, speed):
        if direction == 1:
            return min(self.screen_height - obj_height, obj_y + speed)
        elif direction == -1:
            return max(0, obj_y - speed)
        elif direction == 0:
            return obj_y
        else:
            raise TypeError("direction must be 1, (-1) or 0!")

    def update_players(self):
        self.player_1.rect.y = self.player_1.y
        self.player_2.rect.y = self.player_2.y

    def update_ball(self):
        self.ball.x = self.change_x(self.ball.x, self.ball.width, self.ball.h_direction, self.ball.h_speed)
        self.ball.rect.x = self.ball.x

        self.ball.y = self.change_y(self.ball.y, self.ball.height, self.ball.v_direction, self.ball.v_speed)
        self.ball.rect.y = self.ball.y
        
        if self.ball.y == 0:
            self.ball.v_direction = -self.ball.v_direction
        elif self.ball.y == self.screen_height - self.ball.height:
            self.ball.v_direction = -self.ball.v_direction

    def detect_ball_collision(self):
        part = self.player_height // 5

        if self.ball.rect.colliderect(self.player_1.rect) or self.ball.rect.colliderect(self.player_2.rect):
            if 0 <= self.ball.y < part: # or part <= self.ball.y < part * 2:
                self.ball.v_direction = -1
            # elif part * 2 <= self.ball.y < part * 3:
            #     self.ball.v_direction = 0
            # elif part * 3 <= self.ball.y < part * 4 or part * 4 <= self.ball.y < part * 5:
            #     self.ball.v_direction = 1
            self.ball.h_direction = -self.ball.h_direction

        # if self.ball.rect.colliderect(self.player_1.rect) or self.ball.rect.colliderect(self.player_2.rect):
        #     self.ball.h_direction = -self.ball.h_direction

    def detect_goal(self):
        if self.ball.x == 0 or self.ball.x == self.screen_width - self.ball.width:
            self.restart()

    def restart(self):
        self.ball.x = self.screen_width // 2 - self.ball.width // 2
        self.ball.y = self.screen_height // 2 -self.ball.height // 2
        self.ball.v_direction = 0
        self.ball.h_direction = choice([-1, 1])
