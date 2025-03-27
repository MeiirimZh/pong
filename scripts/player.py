import pygame


class Player:
    def __init__(self, width: int, height: int, screen_height: int, x: int, speed: int, controllable: bool):
        self.width = width
        self.height = height
        self.x = x
        self.y = screen_height // 2 - self.height // 2
        self.speed = speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.controllable = controllable
