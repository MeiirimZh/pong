import pygame


class Data:
    def __init__(self):
        pygame.font.init()
        pygame.mixer.init()

        self.on_fullscreen = False

        self.bg_color = (0, 0, 0)
        self.player_1_color = (255, 255, 255)
        self.player_2_color = (255, 255, 255)
        self.ball_color = (255, 255, 255)
        self.scores_color = (50, 50, 50)
        self.divider_color = (50, 50, 50)

        self.score_font = pygame.font.Font("fonts/Silkscreen-Regular.ttf", 50)
        self.title_font = pygame.font.Font("fonts/Silkscreen-Regular.ttf", 128)
        self.medium_font = pygame.font.Font("fonts/Silkscreen-Regular.ttf", 60)
        self.menu_option_font = pygame.font.Font("fonts/Silkscreen-Regular.ttf", 32)
        self.setting_font = pygame.font.Font("fonts/Silkscreen-Regular.ttf", 24)
        self.credits_font = pygame.font.Font("fonts/Silkscreen-Regular.ttf", 12)

        self.player = "Player 1"

        self.player_speed = 7
        self.computer_speed = 7
        self.ball_h_speed = 5
        self.ball_v_speed = 5

        self.beep_sound = pygame.mixer.Sound("sounds/beep.mp3")
        self.goal_sound = pygame.mixer.Sound("sounds/goal.mp3")
        self.select_sound = pygame.mixer.Sound("sounds/select.mp3")
