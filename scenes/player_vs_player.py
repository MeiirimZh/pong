import pygame

from scenes.default_game_scene import DefaultGameScene


class PlayerVsPlayer(DefaultGameScene):
    def __init__(self, game_state_manager, data, display):
        super().__init__(game_state_manager, data, display)

    def run(self, events):
        super().run(events)

        keys = pygame.key.get_pressed()
        self.handle_player_1_input(keys)
        self.handle_player_2_input(keys)
