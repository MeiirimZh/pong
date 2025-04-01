import pygame

from scenes.default_game_scene import DefaultGameScene


class PlayerVsComputer(DefaultGameScene):
    def __init__(self, game_state_manager, data, display):
        super().__init__(game_state_manager, data, display)

        self.player_handlers = {"Player 1": self.handle_player_1_input, "Player 2": self.handle_player_2_input}

        if self.data.player == "Player 1":
            self.player_2.speed = self.data.computer_speed
        else:
            self.player_1.speed = self.data.computer_speed

    def run(self, events):
        super().run(events)

        keys = pygame.key.get_pressed()
        self.player_handlers[self.data.player](keys)
        self.update_computer()
