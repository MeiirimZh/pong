import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT


class Settings:
    def __init__(self, game_state_manager, data, display):
        self.game_state_manager = game_state_manager
        self.data = data
        self.display = display

        self.distance_color_channels = 80

        self.title = self.data.medium_font.render("Settings", True, (255, 255, 255))

        self.options = ["Fullscreen", "Background color", "Player 1 color", 
                        "Player 2 color", "Ball color", "Return to menu"]
        self.option_pos = [(400, 400), (400, 440), (400, 480), (400, 520), (400, 560),(400, 600)]
        self.current_option = 0

        self.color_channel = 0

        self.change_bg = False

    def run(self, events):
        self.render()

        self.options[0] = 'Fullscreen: ON' if self.data.on_fullscreen else 'Fullscreen: OFF'

        for event in events:
            if event.type == pygame.KEYDOWN:
                self.handle_option_switch(event)
                self.handle_color_channel_switch(event)
                if event.unicode.isdigit():
                    if self.current_option in range(1, 5):
                        self.enter_number(self.current_option, self.color_channel, event.unicode)
                if event.key == pygame.K_BACKSPACE:
                    if self.current_option in range(1, 5):
                        self.delete_number(self.current_option, self.color_channel)
                if event.key == pygame.K_RETURN:
                    if self.current_option == 0:
                        self.data.on_fullscreen = not self.data.on_fullscreen
                        if self.data.on_fullscreen:
                            self.display = self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
                        else:
                            self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    if self.current_option == len(self.options)-1:
                        self.game_state_manager.set_state("Main Menu")

    def handle_option_switch(self, event):
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.current_option = max(0, self.current_option - 1)
            self.data.select_sound.play()
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.current_option = min(len(self.options) - 1, self.current_option + 1)
            self.data.select_sound.play()

    def handle_color_channel_switch(self, event):
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.color_channel = max(0, self.color_channel - 1)
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.color_channel = min(2, self.color_channel + 1)

    def render(self):
        self.display.fill((0, 0, 0))

        self.display.blit(self.title, (477, 40))

        for option in self.options:
            if option == self.options[self.current_option]:
                text = self.data.setting_font.render(option, True, (255, 0, 0))
            else:
                text = self.data.setting_font.render(option, True, (255, 255, 255))
            self.display.blit(text, self.option_pos[self.options.index(option)])

        self.render_color_channels(1, self.data.bg_color, 750, 440)
        self.render_color_channels(2, self.data.player_1_color, 750, 480)
        self.render_color_channels(3, self.data.player_2_color, 750, 520)
        self.render_color_channels(4, self.data.ball_color, 750, 560)

    def enter_number(self, option, color_channel, event_unicode):
        if option == 1:
            current_number = self.data.bg_color[color_channel]
        elif option == 2:
            current_number = self.data.player_1_color[color_channel]
        elif option == 3:
            current_number = self.data.player_2_color[color_channel]
        elif option == 4:
            current_number = self.data.ball_color[color_channel]
        
        if self.can_change_channel(current_number):
            if current_number == 0:
                current_number = event_unicode
            else:
                current_number = str(current_number) + event_unicode

                if int(current_number) > 255:
                    current_number = 255

        if option == 1:
            self.data.bg_color[color_channel] = int(current_number)
        elif option == 2:
            self.data.player_1_color[color_channel] = int(current_number)
        elif option == 3:
            self.data.player_2_color[color_channel] = int(current_number)
        elif option == 4:
            self.data.ball_color[color_channel] = int(current_number)

    def can_change_channel(self, channel):
        return len(str(channel)) != 3

    def delete_number(self, option, color_channel):
        if option == 1:
            current_number = self.data.bg_color[color_channel]
        elif option == 2:
            current_number = self.data.player_1_color[color_channel]
        elif option == 3:
            current_number = self.data.player_2_color[color_channel]
        elif option == 4:
            current_number = self.data.ball_color[color_channel]

        if len(str(current_number)) == 1:
            current_number = 0
        else:
            current_number = int(str(current_number)[:-1])

        if option == 1:
            self.data.bg_color[color_channel] = current_number
        elif option == 2:
            self.data.player_1_color[color_channel] = current_number
        elif option == 3:
            self.data.player_2_color[color_channel] = int(current_number)
        elif option == 4:
            self.data.ball_color[color_channel] = int(current_number)

    def render_color_channels(self, current_option, color, x, y):
        for i in range(3):
            if i == self.color_channel and self.current_option == current_option:
                text = self.data.setting_font.render(str(color[i]), True, (255, 0, 0))
            else:
                text = self.data.setting_font.render(str(color[i]), True, (255, 255, 255))
            self.display.blit(text, (x + i * self.distance_color_channels, y))
