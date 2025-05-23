import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT, SETTINGS_PATH
from scripts.utils import place_options_vertical


class Settings:
    def __init__(self, game_state_manager, data, display, player_vs_player, player_vs_computer):
        self.game_state_manager = game_state_manager
        self.data = data
        self.display = display

        self.distance_color_channels = 80

        self.title = self.data.medium_font.render("Settings", True, (255, 255, 255))

        self.fullscreen_text = "Fullscreen"
        self.reset_text = "Reset settings"
        self.save_text = "Save settings"
        self.return_text = "Return to menu"

        self.options = [self.fullscreen_text, "Player side", "Background color", "Player 1 color", 
                        "Player 2 color", "Ball color", "Scores text color", 
                        "Divider color", self.reset_text, self.save_text, self.return_text]

        self.option_pos = []
        place_options_vertical(self.options, self.option_pos, 400, 200, 40)

        self.current_option = 0

        self.color_channel = 0

        self.sides = ("left", "right")
        self.side = 0 if self.data.player == "Player 1" else 1

        self.pvp = player_vs_player
        self.pvc = player_vs_computer

    def run(self, events):
        self.render()

        self.options[0] = 'Fullscreen: ON' if self.data.on_fullscreen else 'Fullscreen: OFF'
        self.fullscreen_text = self.options[0]

        for event in events:
            if event.type == pygame.KEYDOWN:
                self.handle_option_switch(event)
                if self.current_option in range(2, 8):
                    self.handle_color_channel_switch(event)
                if self.current_option == 1:
                    self.handle_side_switch(event)
                if event.unicode.isdigit():
                    if self.current_option in range(2, 8):
                        self.enter_number(self.current_option, self.color_channel, event.unicode)
                if event.key == pygame.K_BACKSPACE:
                    if self.current_option in range(2, 8):
                        self.delete_number(self.current_option, self.color_channel)
                if event.key == pygame.K_RETURN:
                    if self.options[self.current_option] == self.fullscreen_text:
                        self.data.on_fullscreen = not self.data.on_fullscreen
                        if self.data.on_fullscreen:
                            self.display = self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
                        else:
                            self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    if self.options[self.current_option] == self.reset_text:
                        self.reset_settings()
                    if self.options[self.current_option] == self.save_text:
                        self.save_settings()
                    if self.options[self.current_option] == self.return_text:
                        self.game_state_manager.set_state("Main Menu")

    def handle_option_switch(self, event):
        if event.key in (self.data.player_1_up, self.data.player_2_up):
            self.current_option = max(0, self.current_option - 1)
            self.data.select_sound.play()
        if event.key in (self.data.player_1_down, self.data.player_2_down):
            self.current_option = min(len(self.options) - 1, self.current_option + 1)
            self.data.select_sound.play()

    def handle_color_channel_switch(self, event):
        if event.key in (self.data.sett_swch_left_1, self.data.sett_swch_left_2):
            self.color_channel = max(0, self.color_channel - 1)
        if event.key in (self.data.sett_swch_right_1, self.data.sett_swch_right_2):
            self.color_channel = min(2, self.color_channel + 1)

    def handle_side_switch(self, event):
        if event.key in (self.data.sett_swch_left_1, self.data.sett_swch_left_2):
            self.side = 0
            self.data.player = "Player 2" if self.data.player == "Player 1" else "Player 1"
        if event.key in (self.data.sett_swch_right_1, self.data.sett_swch_right_2):
            self.side = 1
            self.data.player = "Player 2" if self.data.player == "Player 1" else "Player 1"

    def render(self):
        self.display.fill((0, 0, 0))

        self.display.blit(self.title, (477, 40))

        for option in self.options:
            if option == self.options[self.current_option]:
                text = self.data.setting_font.render(option, True, (255, 0, 0))
            else:
                text = self.data.setting_font.render(option, True, (255, 255, 255))
            self.display.blit(text, self.option_pos[self.options.index(option)])

        for i in range(2):
            if self.side == i and self.current_option == 1:
                text = self.data.setting_font.render(self.sides[i], True, (255, 0, 0))
            else:
                text = self.data.setting_font.render(self.sides[i], True, (255, 255, 255))
            self.display.blit(text, (750 + i * 80, 240))

        self.render_color_channels(2, self.data.bg_color, 750, self.option_pos[2][1])
        self.render_color_channels(3, self.data.player_1_color, 750, self.option_pos[3][1])
        self.render_color_channels(4, self.data.player_2_color, 750, self.option_pos[4][1])
        self.render_color_channels(5, self.data.ball_color, 750, self.option_pos[5][1])
        self.render_color_channels(6, self.data.scores_color, 750, self.option_pos[6][1])
        self.render_color_channels(7, self.data.divider_color, 750, self.option_pos[7][1])

    def enter_number(self, option, color_channel, event_unicode):
        if option == 2:
            current_number = self.data.bg_color[color_channel]
        elif option == 3:
            current_number = self.data.player_1_color[color_channel]
        elif option == 4:
            current_number = self.data.player_2_color[color_channel]
        elif option == 5:
            current_number = self.data.ball_color[color_channel]
        elif option == 6:
            current_number = self.data.scores_color[color_channel]
            self.update_scores_color()
        elif option == 7:
            current_number = self.data.divider_color[color_channel]
        
        if self.can_change_channel(current_number):
            if current_number == 0:
                current_number = event_unicode
            else:
                current_number = str(current_number) + event_unicode

                if int(current_number) > 255:
                    current_number = 255

        if option == 2:
            self.data.bg_color[color_channel] = int(current_number)
        elif option == 3:
            self.data.player_1_color[color_channel] = int(current_number)
        elif option == 4:
            self.data.player_2_color[color_channel] = int(current_number)
        elif option == 5:
            self.data.ball_color[color_channel] = int(current_number)
        elif option == 6:
            self.data.scores_color[color_channel] = int(current_number)
            self.update_scores_color()
        elif option == 7:
            self.data.divider_color[color_channel] = int(current_number)

    def can_change_channel(self, channel):
        return len(str(channel)) != 3

    def delete_number(self, option, color_channel):
        if option == 2:
            current_number = self.data.bg_color[color_channel]
        elif option == 3:
            current_number = self.data.player_1_color[color_channel]
        elif option == 4:
            current_number = self.data.player_2_color[color_channel]
        elif option == 5:
            current_number = self.data.ball_color[color_channel]
        elif option == 6:
            current_number = self.data.scores_color[color_channel]
            self.update_scores_color()
        elif option == 7:
            current_number = self.data.divider_color[color_channel]

        if len(str(current_number)) == 1:
            current_number = 0
        else:
            current_number = int(str(current_number)[:-1])

        if option == 2:
            self.data.bg_color[color_channel] = current_number
        elif option == 3:
            self.data.player_1_color[color_channel] = current_number
        elif option == 4:
            self.data.player_2_color[color_channel] = current_number
        elif option == 5:
            self.data.ball_color[color_channel] = current_number
        elif option == 6:
            self.data.scores_color[color_channel] = current_number
            self.update_scores_color()
        elif option == 7:
            self.data.divider_color[color_channel] = current_number

    def render_color_channels(self, current_option, color, x, y):
        for i in range(3):
            if i == self.color_channel and self.current_option == current_option:
                text = self.data.setting_font.render(str(color[i]), True, (255, 0, 0))
            else:
                text = self.data.setting_font.render(str(color[i]), True, (255, 255, 255))
            self.display.blit(text, (x + i * self.distance_color_channels, y))

    def update_scores_color(self):
        self.pvp.player_1_score_text = self.data.score_font.render(str(self.pvp.player_1_scores), 
                                                                   True, self.data.scores_color)
        self.pvp.player_2_score_text = self.data.score_font.render(str(self.pvp.player_2_scores), 
                                                                   True, self.data.scores_color)
        self.pvc.player_1_score_text = self.data.score_font.render(str(self.pvc.player_1_scores), 
                                                                   True, self.data.scores_color)
        self.pvc.player_2_score_text = self.data.score_font.render(str(self.pvc.player_2_scores), 
                                                                   True, self.data.scores_color)

    def reset_settings(self):
        self.data.on_fullscreen = False
        self.data.bg_color = [0, 0, 0]
        self.data.player_1_color = [255, 255, 255]
        self.data.player_2_color = [255, 255, 255]
        self.data.ball_color = [255, 255, 255]
        self.data.scores_color = [50, 50, 50]
        self.data.divider_color = [50, 50, 50]
        self.data.player = "Player 1"
        self.update_scores_color()

        self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.side = 0

    def save_settings(self):
        settings = self.data.load_data(SETTINGS_PATH)
        settings['on_fullscreen'] = self.data.on_fullscreen
        settings['bg_color'] = self.data.bg_color
        settings['player_1_color'] = self.data.player_1_color
        settings['player_2_color'] = self.data.player_2_color
        settings['ball_color'] = self.data.ball_color
        settings['scores_color'] = self.data.scores_color
        settings['divider_color'] = self.data.divider_color
        settings['player'] = self.data.player
        self.data.save_data(SETTINGS_PATH, settings)
