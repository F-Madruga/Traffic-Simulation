import pygame
import constants
from pygame.math import Vector2
from actormodel.actor import Actor
from actormodel.message import Message


class TrafficLight(Actor):
    count = 0
    def __init__(self, x, y, blocks, radius=constants.TRAFFIC_LIGHT_SIZE):
        self.id = TrafficLight.count
        TrafficLight.count += 1
        self.blocks = blocks
        self.position = Vector2(x, y)
        self.radius = radius
        self.approaching_cars = []
        self.stopped_cars = []
        self.cars_on_intersect = []
        self.colors = [constants.GREEN for i in range(4)]
        super().__init__()

    def display(self, screen):

        pygame.draw.polygon(screen, self.colors[0], ((self.position[0], self.position[1]),
                                                      (self.position[0] - (self.radius / 2), self.position[1] - (self.radius / 2)),
                                                      (self.position[0] - self.radius, self.position[1]),
                                                      (self.position[0] - (self.radius / 2), self.position[1] + (self.radius / 2))))
        pygame.draw.polygon(screen, self.colors[2], ((self.position[0], self.position[1]),
                                                      (self.position[0] + (self.radius / 2), self.position[1] - (self.radius / 2)),
                                                      (self.position[0] + self.radius, self.position[1]),
                                                      (self.position[0] + (self.radius / 2),self.position[1] + (self.radius / 2))))
        pygame.draw.polygon(screen, self.colors[1], ((self.position[0], self.position[1]),
                                                    (self.position[0] + (self.radius / 2), self.position[1] - (self.radius / 2)),
                                                    (self.position[0], self.position[1] - self.radius),
                                                    (self.position[0] - (self.radius / 2), self.position[1] - (self.radius / 2))))
        pygame.draw.polygon(screen, self.colors[3], ((self.position[0], self.position[1]),
                                                    (self.position[0] + (self.radius / 2),self.position[1] + (self.radius / 2)),
                                                    (self.position[0], self.position[1] + self.radius),
                                                    (self.position[0] - (self.radius / 2), self.position[1] + (self.radius / 2))))

    def handle_intersect(self):
        for i in range(1, len(self.blocks)):
            for car in self.blocks[i][3]:
                if car.position[0] > self.position[0] and car.angle == 90 \
                    or car.position[0] < self.position[0] and car.angle == 270 \
                    or car.position[1] > self.position[1] and car.angle == 180 \
                    or car.position[1] < self.position[1] and car.angle == 0:
                    if car not in self.approaching_cars:
                        self.approaching_cars.append(car)
        
        for car in self.blocks[0][3]:
            if car in self.approaching_cars:
                self.approaching_cars.remove(car)
                self.stopped_cars.append(car)
                if car.angle == 0:
                    self.colors[1] = constants.RED
                elif car.angle == 90:
                    self.colors[2] = constants.RED
                elif car.angle == 180:
                    self.colors[3] = constants.RED
                else:
                    self.colors[0] = constants.RED
                print("TrafficLight", self.id, "order to car", car.id, "to stop")
                car.address(Message("Please stop", messageType="stop", replyTo=self.address))
        
        if len(self.stopped_cars) > 0 and len(self.cars_on_intersect) == 0:
            self.cars_on_intersect = self.stopped_cars
            self.stopped_cars = []
            for car in self.cars_on_intersect:
                if car.angle == 0:
                    self.colors[1] = constants.GREEN
                elif car.angle == 90:
                    self.colors[2] = constants.GREEN
                elif car.angle == 180:
                    self.colors[3] = constants.GREEN
                else:
                    self.colors[0] = constants.GREEN
                print("TrafficLight", self.id, "gave permission to", car.id, "to move")
                car.address(Message("You can move", messageType="go", replyTo=self.address))

        for car in self.cars_on_intersect:
            if car not in self.blocks[0][3]:
                self.cars_on_intersect.remove(car)
    
    def handle_message(self, message):
        print("TrafficLight", self.id, "receive message:", message.content)