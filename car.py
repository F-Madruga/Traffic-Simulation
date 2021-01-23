import pygame
import constants
from actormodel.actor import Actor
from pygame.math import Vector2
from math import sin, cos, radians


class Car(Actor):
    count = 0
    def __init__(self, x, y, angle, velocity=Vector2(0.0, 0.1), radius=constants.SIZE):
        self.id = Car.count
        Car.count += 1
        self.radius = radius
        self.position = Vector2(x, y)
        self.velocity = velocity
        self.angle = angle
        super().__init__()
    
    def __str__(self):
     return "Car={id=" + str(self.id) + ", position=" + str(self.position) + ", velocity=" + str(self.velocity) + ", radius=" + str(self.radius) + "}"

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

    def move(self, blocks):
        front_block_y = 1 + int(cos(radians(self.angle)))
        front_block_x = 1 - int(sin(radians(self.angle)))
        if blocks[front_block_y][front_block_x][1] == constants.BLACK:
            block_center_x = blocks[front_block_y][front_block_x][0].x + (blocks[front_block_y][front_block_x][0].width / 2)
            block_center_y = blocks[front_block_y][front_block_x][0].y + (blocks[front_block_y][front_block_x][0].height / 2)
            if self.angle == 90:
                if self.position[0] <= block_center_x: # + blocks[0][0][0].width / 4:
                    self.move_down()
            elif self.angle == -90:
                if self.position[0] >= block_center_x: # + blocks[0][0][0].width / 4:
                    self.move_up()
            elif self.angle == 0:
                if self.position[1] >= block_center_y: # + blocks[0][0][0].height / 4:
                    self.move_right()
            elif self.angle == 180:
                if self.position[1] <= block_center_y: # + blocks[0][0][0].height / 4:
                    self.move_left()

        self.position += self.velocity.rotate(self.angle)
    
    def handle_message(self, message):
        pass