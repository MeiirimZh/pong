import pygame


class DefaultGameScene:
    def __init__(self, game_state_manager, data, display):
        self.game_state_manager = game_state_manager
        self.data = data
        self.display = display

        self.player_width = 20
        self.player_height = 100

        self.screen_center = display.get_size()[1] // 2 - self.player_height // 2

        self.player_1_x = 100
        self.player_1_y = self.screen_center

        self.player_2_x = display.get_size()[0] - 100 - self.player_width
        self.player_2_y = self.screen_center

        self.player_1_rect = pygame.Rect(self.player_1_x, self.player_1_y, self.player_width, self.player_height)
        self.player_2_rect = pygame.Rect(self.player_2_x, self.player_2_y, self.player_width, self.player_height)

    def render(self):
        pygame.draw.rect(self.display, self.data.player_1_color, self.player_1_rect)
        pygame.draw.rect(self.display, self.data.player_2_color, self.player_2_rect)
