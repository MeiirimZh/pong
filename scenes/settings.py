import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT


class Settings:
    def __init__(self, game_state_manager, data, display):
        self.game_state_manager = game_state_manager
        self.data = data
        self.display = display

        self.title = self.data.medium_font.render("Settings", True, (255, 255, 255))

        self.options = ["Fullscreen", "Background color", "Return to menu"]
        self.option_pos = [(400, 400), (400, 460), (400, 520)]
        self.current_option = 0

    def run(self, events):
        self.display.fill((0, 0, 0))

        self.display.blit(self.title, (477, 40))

        self.options[0] = 'Fullscreen: ON' if self.data.on_fullscreen else 'Fullscreen: OFF'

        for option in self.options:
            if option == self.options[self.current_option]:
                text = self.data.setting_font.render(option, True, (255, 0, 0))
            else:
                text = self.data.setting_font.render(option, True, (255, 255, 255))
            self.display.blit(text, self.option_pos[self.options.index(option)])

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.current_option = max(0, self.current_option - 1)
                    self.data.select_sound.play()
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.current_option = min(len(self.options) - 1, self.current_option + 1)
                    self.data.select_sound.play()
                if event.key == pygame.K_RETURN:
                    if self.current_option == 0:
                        self.data.on_fullscreen = not self.data.on_fullscreen
                        if self.data.on_fullscreen:
                            self.display = self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
                        else:
                            self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    if self.current_option == 2:
                        self.game_state_manager.set_state("Main Menu")
