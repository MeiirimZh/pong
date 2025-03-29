import pygame


class Ball:
    def __init__(self, width: int, height: int, screen_width: int, screen_height: int, 
                 h_speed: int, v_speed: int, h_direction: int, v_direction: int):
        self.width = width
        self.height = height
        self.x = screen_width // 2 - self.width // 2
        self.y = screen_height // 2 - self.height // 2
        self.h_speed = h_speed
        self.v_speed = v_speed
        self.h_direction = h_direction
        self.v_direction = v_direction
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
