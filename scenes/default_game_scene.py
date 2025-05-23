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

        self.ball_start_h_direction = choice([-1, 1]) 
        self.ball_start_v_direction = choice([-1, 1])

        self.player_height = 150
        self.player_1 = Player(20, self.player_height, self.screen_height, 100, self.data.player_speed)
        self.player_2 = Player(20, self.player_height, self.screen_height, 1160, self.data.player_speed)
        self.ball = Ball(30, 30, self.screen_width, self.screen_height, self.data.ball_h_speed, self.data.ball_v_speed,
                        self.ball_start_h_direction, self.ball_start_v_direction)

        self.player_1_scores = 0
        self.player_2_scores = 0
        self.player_1_score_text = self.data.score_font.render(str(self.player_1_scores), True, self.data.scores_color)
        self.player_2_score_text = self.data.score_font.render(str(self.player_2_scores), True, self.data.scores_color)

        self.rounds = 0

        self.divider = pygame.Rect(638, 0, 4, 720)

    def run(self, events):
        self.render()
        self.update_players()
        self.update_ball()
        self.detect_ball_collision()
        self.detect_goal()

    def render(self):
        self.display.blit(self.player_1_score_text, (self.p1_score_pos(), 329))
        self.display.blit(self.player_2_score_text, (660, 329))
        pygame.draw.rect(self.display, self.data.divider_color, self.divider)
        pygame.draw.rect(self.display, self.data.player_1_color, self.player_1.rect)
        pygame.draw.rect(self.display, self.data.player_2_color, self.player_2.rect)
        pygame.draw.rect(self.display, self.data.ball_color, self.ball.rect)

    def handle_player_1_input(self, keys):
        if keys[self.data.player_1_up]:
            self.player_1.y = self.change_y(self.player_1.y, self.player_1.height, -1, self.player_1.speed)
        if keys[self.data.player_1_down]:
            self.player_1.y = self.change_y(self.player_1.y, self.player_1.height, 1, self.player_1.speed)

    def handle_player_2_input(self, keys):
        if keys[self.data.player_2_up]:
            self.player_2.y = self.change_y(self.player_2.y, self.player_2.height, -1, self.player_2.speed)
        if keys[self.data.player_2_down]:
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
        self.ball.y = self.change_y(self.ball.y, self.ball.height, self.ball.v_direction, self.ball.v_speed)

        self.ball.rect.x = self.ball.x
        self.ball.rect.y = self.ball.y

        if self.ball.y == 0 or self.ball.y == self.screen_height - self.ball.height:
            self.ball.v_direction = -self.ball.v_direction

    def update_computer(self):
        if self.data.player == "Player 1":
            self.move_computer(self.player_2)
        else:
            self.move_computer(self.player_1)

    def move_computer(self, computer):
        if 0 < computer.y - self.ball.y < 100:
            computer.y = self.change_y(computer.y, computer.height, -1, computer.speed // 2)
        elif 100 < computer.y - self.ball.y:
            computer.y = self.change_y(computer.y, computer.height, -1, computer.speed)
        elif computer.y == self.ball.y:
            pass
        elif 0 < self.ball.y - computer.y < 100:
            computer.y = self.change_y(computer.y, computer.height, 1, computer.speed // 2)
        else:
            computer.y = self.change_y(computer.y, computer.height, 1, computer.speed)

    def detect_ball_collision(self):
        parts_count = 5
        ball_collided = False

        if self.ball.rect.colliderect(self.player_1.rect):
            collide_part = self.what_part_of_x_is_y_in(self.player_1.height, self.player_1.y, self.ball.height, self.ball.y, parts_count)
            ball_collided = True

        if self.ball.rect.colliderect(self.player_2.rect):
            collide_part = self.what_part_of_x_is_y_in(self.player_2.height, self.player_2.y, self.ball.height, self.ball.y, parts_count)
            ball_collided = True

        if ball_collided:
            if collide_part in (1, 2):
                self.ball.v_direction = -1
            elif collide_part == 3:
                self.ball.v_direction = 0
            else:
                self.ball.v_direction = 1
            self.ball.h_direction = -self.ball.h_direction
            self.data.beep_sound.play()

    def what_part_of_x_is_y_in(self, obj_1_height, obj_1_y, obj_2_height, obj_2_y, parts_count):
        part = obj_1_height // parts_count

        if obj_1_y - obj_2_height <= obj_2_y < obj_1_y + part:
            return 1
        
        if obj_1_y + part * parts_count - 1 <= obj_2_y < obj_1_y + part * parts_count + obj_2_height:
            return parts_count

        for i in range(1, part-1):
            if obj_1_y + i * part <= obj_2_y < obj_1_y + (i+1) * part:
                return i + 1

    def detect_goal(self):
        if self.ball.x == 0 or self.ball.x == self.screen_width - self.ball.width:
            self.restart()
            self.data.goal_sound.play()

    def restart(self):
        self.rounds += 1

        if self.ball.x == 0:
            self.ball.h_direction = -1
            self.player_2_win(1)
        else:
            self.ball.h_direction = 1
            self.player_1_win(1)

        self.restart_ball()

    def restart_ball(self):
        self.ball.x = self.screen_width // 2 - self.ball.width // 2
        self.ball.y = self.screen_height // 2 -self.ball.height // 2
        self.ball.v_direction = choice([-1, 1])
        self.ball.h_speed = self.data.ball_h_speed + self.rounds // 5
        self.ball.v_speed = self.data.ball_v_speed + self.rounds // 5

    def p1_score_pos(self):
        return 620 - self.data.score_font.size(str(self.player_1_scores))[0]
    
    def player_1_win(self, scores):
        self.player_1_scores += scores
        self.player_1_score_text = self.data.score_font.render(str(self.player_1_scores), True, self.data.scores_color)

    def player_2_win(self, scores):
        self.player_2_scores += scores
        self.player_2_score_text = self.data.score_font.render(str(self.player_2_scores), True, self.data.scores_color)
