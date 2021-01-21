import pygame
from actormodel.Actor import Actor


class Car(Actor):
    def __init__(self, x, y, velocity=0.1):
        self.x = x
        self.y = y
        self.velocity = velocity
        super().__init__()

    def display(self, screen):
        pygame.draw.circle(screen, (255,0,0) , [self.x, self.y], 10)

    def move_right(self):
        self.x += self.velocity
    
    def move_left(self):
        self.x -= self.velocity

    def move_up(self):
        self.y -= self.velocity
    
    def move_down(self):
        self.y += self.velocity
    
    def handleMessage(self, message):
        pass