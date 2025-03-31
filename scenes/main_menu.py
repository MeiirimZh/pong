import pygame


class MainMenu:
    def __init__(self, game_state_manager, data, display):
        self.game_state_manager = game_state_manager
        self.data = data
        self.display = display

    def run(self):
        self.display.fill((0, 0, 0))
