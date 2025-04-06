import pygame
import json


class Data:
    def __init__(self):
        pygame.font.init()
        pygame.mixer.init()

        self.on_fullscreen = False

        self.bg_color = [0, 0, 0]
        self.player_1_color = [255, 255, 255]
        self.player_2_color = [255, 255, 255]
        self.ball_color = [255, 255, 255]
        self.scores_color = [50, 50, 50]
        self.divider_color = [50, 50, 50]

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
    
    def load_data(self, path):
        with open(path, 'r') as file:
            return json.load(file)
        
    def save_data(self, path, data):
        with open(path, 'w') as file:
            json.dump(data, file, indent=2)

    def set_settings(self, settings):
        self.on_fullscreen = settings['on_fullscreen']
        self.bg_color = settings['bg_color']
        self.player_1_color = settings['player_1_color']
        self.player_2_color = settings['player_2_color']
        self.ball_color = settings['ball_color']
        self.scores_color = settings['scores_color']
        self.divider_color = settings['divider_color']
        self.player = settings['player']
