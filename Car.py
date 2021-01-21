import pygame


class Car:
    def __init__(self, x, y, velocity_x = 0, velocity_y = 0):
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.x = x
        self.y = y

    def display(self, screen):
        pygame.draw.circle(screen, (255,0,0) , [self.x, self.y], 10)

    def move_x(self):
        self.x += self.velocity_x

    def move_y(self):
        self.y += self.velocity_y