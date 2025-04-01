import pygame


class MainMenu:
    def __init__(self, game_state_manager, data, display):
        self.game_state_manager = game_state_manager
        self.data = data
        self.display = display

        self.title = self.data.title_font.render("PONG", True, (255, 255, 255))

        self.options = ["Player vs Player", "Player vs Computer", "Settings", "Exit"]
        self.option_pos = [(520, 340), (492, 399), (577, 458), (612, 517)]
        self.current_option = 0

    def run(self, events):
        self.display.fill((0, 0, 0))

        self.display.blit(self.title, (454, 80))

        for option in self.options:
            if option == self.options[self.current_option]:
                text = self.data.menu_option_font.render(option, True, (255, 0, 0))
            else:
                text = self.data.menu_option_font.render(option, True, (255, 255, 255))
            self.display.blit(text, self.option_pos[self.options.index(option)])

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.current_option = max(0, self.current_option - 1)
                if event.key == pygame.K_DOWN:
                    self.current_option = min(len(self.options) - 1, self.current_option + 1)
