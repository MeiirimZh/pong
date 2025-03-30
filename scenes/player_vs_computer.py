import pygame

from scenes.default_game_scene import DefaultGameScene


class PlayerVsComputer(DefaultGameScene):
    def __init__(self, game_state_manager, data, display):
        super().__init__(game_state_manager, data, display)

        self.player_handlers = {"Player 1": self.handle_player_1_input, "Player 2": self.handle_player_2_input}

    def run(self):
        super().run()

        keys = pygame.key.get_pressed()
        self.player_handlers[self.data.player](keys)
