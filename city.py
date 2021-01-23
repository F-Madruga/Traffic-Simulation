import pygame
import random
import constants
from car import Car

class City():
    def __init__(self, blocks, checkpoints, num_cars=constants.CARS_NUMBER):
        self.blocks = blocks
        self.checkpoints = checkpoints
        self.cars = []
        for i in range(num_cars):
            checkpoint = self.checkpoints[random.randint(0, len(checkpoints) - 1)]
            block = self.blocks[checkpoint[0]][checkpoint[1]]
            # (Up, Down, Left, Right)
            neighbours = (
                self.blocks[checkpoint[0] - 1][checkpoint[1]][1] == constants.BLACK,
                self.blocks[checkpoint[0] + 1][checkpoint[1]][1] == constants.BLACK,
                self.blocks[checkpoint[0]][checkpoint[1] - 1][1] == constants.BLACK,
                self.blocks[checkpoint[0]][checkpoint[1] + 1][1] == constants.BLACK,
            )
            colors = (
                self.blocks[checkpoint[0] - 1][checkpoint[1]][1],
                self.blocks[checkpoint[0] + 1][checkpoint[1]][1],
                self.blocks[checkpoint[0]][checkpoint[1] - 1][1],
                self.blocks[checkpoint[0]][checkpoint[1] + 1][1],
            )
            x = block[0].x
            y = block[0].y
            direction = random.randint(0, 1)
            if direction == 0:
                x += (block[0].width / 4.0)
                y += (block[0].height / 4.0)
            else:
                x += (block[0].width * 3.0 / 4.0)
                y += (block[0].height * 3.0 / 4.0)
            angle = 0
            print(colors)
            print(neighbours)
            if neighbours == (True, True, False, False) \
                or neighbours == (False, True, False, False) \
                or neighbours == (True, False, False, False):
                if direction == 0:
                    angle = 90
                else:
                    angle = -90
            elif neighbours == (False, False, True, True) \
                or neighbours == (False, False, True, False) \
                or neighbours == (False, False, False, True):
                if direction == 0:
                    angle = 0
                else:
                    angle = 180
            # elif neighbours == (True, False, True, False):
            #     if direction == 0:
            #         angle = 0
            #     else:
            #         angle = -90
            # elif neighbours == (True, False, False, True):
            #     if direction == 0:
            #         angle = 90
            #     else:
            #         angle = 180
            # elif neighbours == (False, True, True, False):
            #     if direction == 0:
            #         angle = 0
            #     else:
            #         angle = 180
            # elif neighbours == (False, True, False, True):
            #     if direction == 0:
            #         angle = 90
            #     else:
            #         angle = 180
            self.cars.append(Car(x, y, angle))

    
    @staticmethod
    def read_file(path, screen_width, screen_height):
        matrix = []
        file = open(path, "r")
        lines = file.readlines()
        for line in lines:
            matrix_line = []
            for cell in line:
                if cell != "\n":
                    matrix_line.append(int(cell))
            matrix.append(matrix_line)
        
        blocks = []
        checkpoints = []
        block_width = screen_width / len(matrix[0])
        block_height = screen_height / len(matrix)
        x = 0
        y = 0
        for i in range(len(matrix)):
            blocks_line = []
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    blocks_line.append((pygame.Rect(x, y, block_width, block_height), constants.BLACK))
                elif matrix[i][j] == 1:
                    blocks_line.append((pygame.Rect(x, y, block_width, block_height), constants.WHITE))
                elif matrix[i][j] == 2:
                    blocks_line.append((pygame.Rect(x, y, block_width, block_height), constants.GRAY))
                    checkpoints.append((i, j))
                x += block_width
            blocks.append(blocks_line)
            x = 0
            y += block_height
        return City(blocks, checkpoints)
    
    def __str__(self):
        return "City={blocks=" + str(self.blocks) + ", checkpoints=" + str(self.checkpoints) + "}"
    
    def display(self, screen):
        for blocks_line in self.blocks:
            for blocks in blocks_line:
                pygame.draw.rect(screen, blocks[1], blocks[0])
        for car in self.cars:
            car.display(screen)
            car.move()