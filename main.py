from sys import exit
import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE, FPS
from data import Data
from scenes.main_menu import MainMenu
from scenes.settings import Settings
from scenes.player_vs_computer import PlayerVsComputer
from scenes.player_vs_player import PlayerVsPlayer


class Game:
    def __init__(self):
        self.game_state_manager = GameStateManager("Main Menu")
        self.data = Data()

        pygame.init()
        if self.data.on_fullscreen:
            self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        else:
            self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()

        self.main_menu = MainMenu(self.game_state_manager, self.data, self.display)
        self.player_vs_computer = PlayerVsComputer(self.game_state_manager, self.data, self.display)
        self.player_vs_player = PlayerVsPlayer(self.game_state_manager, self.data, self.display)
        self.settings = Settings(self.game_state_manager, self.data, self.display, self.player_vs_player, self.player_vs_computer)
        self.scenes = {"Main Menu": self.main_menu, "Settings": self.settings,
            "Player vs Computer": self.player_vs_computer, "Player vs Player": self.player_vs_player}

    def run(self):
        while True:
            pygame.mouse.set_visible(False)

            self.display.fill(self.data.bg_color)

            events = pygame.event.get()

            self.scenes[self.game_state_manager.get_state()].run(events)

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_state_manager.set_state("Main Menu")

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
