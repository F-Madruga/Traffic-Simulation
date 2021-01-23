import pygame
import constants
from actormodel.actor import Actor
from pygame.math import Vector2


class Car(Actor):
    def __init__(self, x, y, angle, velocity=Vector2(0.0, 0.01), radius=constants.SIZE):
        self.radius = radius
        self.position = Vector2(x, y)
        self.velocity = velocity
        self.angle = angle
        super().__init__()
    
    def __str__(self):
     return "Car={position=" + str(self.position) + ", velocity=" + str(self.velocity) + ", radius=" + str(self.radius) + "}"

    def display(self, screen):
        pygame.draw.circle(screen, constants.RED , self.position, self.radius)

    def move_right(self):
        self.angle = -90
    
    def move_left(self):
        self.angle = 90

    def move_up(self):
        self.angle = 180
    
    def move_down(self):
        self.angle = 0

    def move(self):
        self.position += self.velocity.rotate(self.angle)
    
    def handle_message(self, message):
        pass