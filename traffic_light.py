import math
import pygame
import constants
from pygame.math import Vector2
from actormodel.actor import Actor
from actormodel.message import Message


class TrafficLight(Actor):
    count = 0
    def __init__(self, x, y, blocks, radius=constants.TRAFFIC_LIGHT_SIZE):
        self.id = TrafficLight.count
        self.blocks = blocks
        self.position = Vector2(x, y)
        self.radius = radius
        self.to_stop = []
        self.stopped = []
        self.on_intersect = []

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

    def handle_intersect(self):
        for car in self.blocks[0][3]:
            if car.id in self.to_stop:
                self.to_stop = [car_id for car_id in self.to_stop if car_id != car.id]
                self.stopped.append(car.id)
                car.address(Message("É favor parar", messageType="stop"))

        if len(self.on_intersect) == 0 and len(self.stopped) > 0:
            car_id = self.stopped.pop(0)
            self.on_intersect.append(car_id)
            for car in self.blocks[0][3]:
                if car.id == car_id:
                    car.address(Message("Pode avançar", messageType="go"))
                    break
        elif len(self.on_intersect) != 0:
            for car_id in self.on_intersect:
                remove = True
                for car in self.blocks[0][3]:
                    if car.id == car_id:
                        remove = False
                        break
                if remove:
                    self.on_intersect = [c for c in self.on_intersect if car_id != c]

        for i in range(1, len(self.blocks)):
            for car in self.blocks[i][3]:
                if car.position[0] > self.position[0] and car.angle == 90 \
                    or car.position[0] < self.position[0] and car.angle == 270 \
                    or car.position[1] > self.position[1] and car.angle == 180 \
                    or car.position[1] < self.position[1] and car.angle == 0:
                    self.to_stop.append(car.id)