import pygame


class Data:
    def __init__(self):
        pygame.font.init()

        self.bg_color = (0, 0, 0)
        self.player_1_color = (255, 255, 255)
        self.player_2_color = (255, 255, 255)
        self.ball_color = (255, 255, 255)
        self.scores_color = (50, 50, 50)
        self.divider_color = (50, 50, 50)

        self.score_font = pygame.font.Font("fonts/Silkscreen-Regular.ttf", 50)
