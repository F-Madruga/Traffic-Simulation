import math
import pygame
import constants
from pygame.math import Vector2
from actormodel.actor import Actor
from actormodel.message import Message


class TrafficLight(Actor):
    count = 0
    def __init__(self, x, y, current_block_id, traffic_light_blocks, radius=constants.TRAFFIC_LIGHT_SIZE):
        self.current_block_id = current_block_id
        self.traffic_light_blocks = traffic_light_blocks
        self.id = TrafficLight.count
        self.position = Vector2(x, y)
        self.radius = radius

    def display(self, screen):

        pygame.draw.polygon(screen, constants.GREEN, ((self.position[0], self.position[1]),
                                                      (self.position[0] - (self.radius / 2), self.position[1] - (self.radius / 2)),
                                                      (self.position[0] - self.radius, self.position[1]),
                                                      (self.position[0] - (self.radius / 2), self.position[1] + (self.radius / 2))))
        pygame.draw.polygon(screen, constants.GREEN, ((self.position[0], self.position[1]),
                                                      (self.position[0] + (self.radius / 2), self.position[1] - (self.radius / 2)),
                                                      (self.position[0] + self.radius, self.position[1]),
                                                      (self.position[0] + (self.radius / 2),self.position[1] + (self.radius / 2))))
        pygame.draw.polygon(screen, constants.RED, ((self.position[0], self.position[1]),
                                                    (self.position[0] + (self.radius / 2), self.position[1] - (self.radius / 2)),
                                                    (self.position[0], self.position[1] - self.radius),
                                                    (self.position[0] - (self.radius / 2), self.position[1] - (self.radius / 2))))
        pygame.draw.polygon(screen, constants.RED, ((self.position[0], self.position[1]),
                                                    (self.position[0] + (self.radius / 2),self.position[1] + (self.radius / 2)),
                                                    (self.position[0], self.position[1] + self.radius),
                                                    (self.position[0] - (self.radius / 2), self.position[1] + (self.radius / 2))))

    def light_stop(self):
        for i in range(len(self.traffic_light_blocks)):
                if len(self.traffic_light_blocks[i][3]) != 0:
                        for car in self.traffic_light_blocks[i][3]:
                            car.address(Message("É favor parar", messageType="light_stop"))