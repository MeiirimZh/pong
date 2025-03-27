from sys import exit
import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE, FPS
from data import Data
from scenes.player_vs_computer import PlayerVsComputer


class Game:
    def __init__(self):
        self.game_state_manager = GameStateManager("Player vs Computer")
        self.data = Data()

        pygame.init()
        self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()

        self.player_vs_computer = PlayerVsComputer(self.game_state_manager, self.data, self.display)
        self.scenes = {"Player vs Computer": self.player_vs_computer}

    def run(self):
        while True:
            pygame.mouse.set_visible(False)

            self.display.fill(self.data.bg_color)

            events = pygame.event.get()

            self.scenes[self.game_state_manager.get_state()].run()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.update()
            self.clock.tick(FPS)


class GameStateManager:
    def __init__(self, current_state: str):
        self.current_state = current_state

    def get_state(self):
        return self.current_state
    
    def set_state(self, state):
        self.current_state = state


if __name__ == '__main__':
    game = Game()
    game.run()
