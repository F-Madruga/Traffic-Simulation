import pygame
import constants

class Traffic_light:
    def __init__(self, x1, y1, x2, y2, color = constants.GREEN):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

    def display(self, screen):
        pygame.draw.line(screen, self.color, [self.x1, self.y1], [self.x2, self.y2], 3)

    def change_color(self, color):
        self.color = color