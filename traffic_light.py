import math
import pygame
import constants
from pygame.math import Vector2
from actormodel.actor import Actor
from actormodel.message import Message


class TrafficLight(Actor):
    count = 0
    def __init__(self, x, y, radius=constants.TRAFFIC_LIGHT_SIZE):
        self.id = TrafficLight.count
        self.position = Vector2(x, y)
        self.radius = radius

    def display(self, screen):
        pygame.draw.rect(screen, constants.RED, pygame.Rect(self.position[0] - self.radius, self.position[1] - self.radius, self.radius, self.radius))
        pygame.draw.rect(screen, constants.GREEN, pygame.Rect(self.position[0], self.position[1] - self.radius, self.radius, self.radius))
        pygame.draw.rect(screen, constants.GREEN, pygame.Rect(self.position[0] - self.radius, self.position[1], self.radius, self.radius))
        pygame.draw.rect(screen, constants.RED, pygame.Rect(self.position[0], self.position[1], self.radius, self.radius))
