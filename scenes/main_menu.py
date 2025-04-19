import pygame

from sys import exit


class MainMenu:
    def __init__(self, game_state_manager, data, display):
        self.game_state_manager = game_state_manager
        self.data = data
        self.display = display

        self.title = self.data.title_font.render("PONG", True, (255, 255, 255))
        self.author = self.data.credits_font.render("Made by Zhanzhumanov Meiirim 2025", True, (255, 255, 255))

        self.pvp_text = "Player vs Player"
        self.pvc_text = "Player vs Computer"
        self.settings_text = "Settings"

        self.options = [self.pvp_text, self.pvc_text, self.settings_text, "Exit"]
        self.option_pos = [(458, 340), (434, 399), (554, 458), (600, 517)]
        self.current_option = 0

    def run(self, events):
        self.display.fill((0, 0, 0))

        self.display.blit(self.title, (440, 80))
        self.display.blit(self.author, (975, 684))

        for option in self.options:
            if option == self.options[self.current_option]:
                text = self.data.menu_option_font.render(option, True, (255, 0, 0))
            else:
                text = self.data.menu_option_font.render(option, True, (255, 255, 255))
            self.display.blit(text, self.option_pos[self.options.index(option)])

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in (self.data.player_1_up, self.data.player_2_up):
                    self.current_option = max(0, self.current_option - 1)
                    self.data.select_sound.play()
                if event.key in (self.data.player_1_down, self.data.player_2_down):
                    self.current_option = min(len(self.options) - 1, self.current_option + 1)
                    self.data.select_sound.play()
                if event.key == pygame.K_RETURN:
                    if self.options[self.current_option] == self.pvp_text:
                        self.game_state_manager.set_state("Player vs Player")
                    elif self.options[self.current_option] == self.pvc_text:
                        self.game_state_manager.set_state("Player vs Computer")
                    elif self.options[self.current_option] == self.settings_text:
                        self.game_state_manager.set_state("Settings")
                    else:
                        pygame.quit()
                        exit()
