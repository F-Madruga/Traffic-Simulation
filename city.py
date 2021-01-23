import pygame
import random
import constants
from car import Car

class City():
    def __init__(self, blocks, checkpoints, num_cars=constants.CARS_NUMBER):
        self.blocks = blocks
        self.checkpoints = checkpoints
        self.cars = []
        for _ in range(num_cars):
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
            # * Cantos
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
            block[2].append(Car(x, y, angle))
            self.blocks[checkpoint[0]][checkpoint[1]] = block
            # self.cars.append(Car(x, y, angle))
            

    
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
                    blocks_line.append([pygame.Rect(x, y, block_width, block_height), constants.BLACK, []])
                elif matrix[i][j] == 1:
                    blocks_line.append([pygame.Rect(x, y, block_width, block_height), constants.WHITE, []])
                elif matrix[i][j] == 2:
                    blocks_line.append([pygame.Rect(x, y, block_width, block_height), constants.GRAY, []])
                    checkpoints.append((i, j))
                x += block_width
            blocks.append(blocks_line)
            x = 0
            y += block_height
        return City(blocks, checkpoints)
    
    def __str__(self):
        return "City={blocks=" + str(self.blocks) + ", checkpoints=" + str(self.checkpoints) + "}"
    
    def get_car_block(self, car):
        block_width = self.blocks[0][0][0].width
        block_height = self.blocks[0][0][0].height
        block_x_index = car.position[0] // block_width
        block_y_index = car.position[1] // block_height
        return (int(block_x_index), int(block_y_index))
    
    def display(self, screen):
        for i in range(len(self.blocks)):
            for j in range(len(self.blocks[i])):
                pygame.draw.rect(screen, self.blocks[i][j][1], self.blocks[i][j][0])
                car_to_keep = []
                for car_index in range(len(self.blocks[i][j][2])):
                    x, y = self.get_car_block(self.blocks[i][j][2][car_index])
                    if x != j or y != i:
                        self.blocks[y][x][2].append(self.blocks[i][j][2][car_index])
                    else:
                        car_to_keep.append(self.blocks[i][j][2][car_index])
                self.blocks[i][j][2] = car_to_keep
        
        for i in range(len(self.blocks)):
            for j in range(len(self.blocks[i])):
                for car_index in range(len(self.blocks[i][j][2])):
                    self.blocks[i][j][2][car_index].display(screen)
                    sub_blocks = []
                    for g in range(y - 1, y + 2):
                        sub_blocks.append(self.blocks[g][x - 1: x + 2])
                    self.blocks[i][j][2][car_index].move(sub_blocks)