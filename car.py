import pygame
import constants
from actormodel.actor import Actor


class Car(Actor):
    def __init__(self, radius, x, y, velocity=0.1):
        self.radius = radius
        self.x = x
        self.y = y
        self.velocity = velocity
        super().__init__()
    
    def __str__(self):
     return "Car={x=" + str(self.x) + ", y=" + str(self.y) + ", velocity=" + str(self.velocity) + ", radius=" + str(self.radius) + "}"

    def display(self, screen):
        pygame.draw.circle(screen, constants.RED , [self.x, self.y], self.radius)

    def move_right(self):
        self.x += self.velocity
    
    def move_left(self):
        self.x -= self.velocity

    def move_up(self):
        self.y -= self.velocity
    
    def move_down(self):
        self.y += self.velocity
    
    def handle_message(self, message):
        pass