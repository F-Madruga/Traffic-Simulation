import pygame
import random
import constants
from car import Car

class City():
    def __init__(self, blocks, checkpoints, num_cars=constants.CARS_NUMBER):
        self.blocks = blocks
        self.checkpoints = checkpoints
        self.generate_cars(checkpoints)
        # for _ in range(num_cars):
        #     checkpoint = self.checkpoints[random.randint(0, len(checkpoints) - 1)]
            
        #     neighbours = (
        #         self.blocks[checkpoint[0] - 1][checkpoint[1]][2] == constants.BLACK,
        #         self.blocks[checkpoint[0] + 1][checkpoint[1]][2] == constants.BLACK,
        #         self.blocks[checkpoint[0]][checkpoint[1] - 1][2] == constants.BLACK,
        #         self.blocks[checkpoint[0]][checkpoint[1] + 1][2] == constants.BLACK,
        #     )
        #     x = self.blocks[checkpoint[0]][checkpoint[1]][1].x
        #     y = self.blocks[checkpoint[0]][checkpoint[1]][1].y
        #     direction = random.randint(0, 1)
        #     if direction == 0:
        #         x += (self.blocks[checkpoint[0]][checkpoint[1]][1].width / 4.0)
        #         y += (self.blocks[checkpoint[0]][checkpoint[1]][1].height / 4.0)
        #     else:
        #         x += (self.blocks[checkpoint[0]][checkpoint[1]][1].width * 3.0 / 4.0)
        #         y += (self.blocks[checkpoint[0]][checkpoint[1]][1].height * 3.0 / 4.0)
            
        #     angle = 0
        #     if neighbours == (True, True, False, False) \
        #         or neighbours == (False, True, False, False) \
        #         or neighbours == (True, False, False, False):
        #         if direction == 0:
        #             angle = 90
        #         else:
        #             angle = 270
        #     elif neighbours == (False, False, True, True) \
        #         or neighbours == (False, False, True, False) \
        #         or neighbours == (False, False, False, True):
        #         if direction == 0:
        #             angle = 0
        #         else:
        #             angle = 180
        #     car = Car(x, y, angle, self.blocks[checkpoint[0]][checkpoint[1]][0])
        #     self.blocks[checkpoint[0]][checkpoint[1]][3].append(car)
    
    def generate_cars(self, checkpoints):
        for checkpoint in checkpoints:
            neighbours = (
                self.blocks[checkpoint[0] - 1][checkpoint[1]][2] == constants.BLACK,
                self.blocks[checkpoint[0] + 1][checkpoint[1]][2] == constants.BLACK,
                self.blocks[checkpoint[0]][checkpoint[1] - 1][2] == constants.BLACK,
                self.blocks[checkpoint[0]][checkpoint[1] + 1][2] == constants.BLACK,
            )
            x0 = self.blocks[checkpoint[0]][checkpoint[1]][1].x + (self.blocks[checkpoint[0]][checkpoint[1]][1].width / 4.0)
            x1 = self.blocks[checkpoint[0]][checkpoint[1]][1].x + (self.blocks[checkpoint[0]][checkpoint[1]][1].width * 3.0 / 4.0)
            y0 = self.blocks[checkpoint[0]][checkpoint[1]][1].y + (self.blocks[checkpoint[0]][checkpoint[1]][1].height / 4.0)
            y1 = self.blocks[checkpoint[0]][checkpoint[1]][1].y + (self.blocks[checkpoint[0]][checkpoint[1]][1].height * 3.0 / 4.0)
            if neighbours == (True, True, False, False) \
                or neighbours == (False, True, False, False) \
                or neighbours == (True, False, False, False):
                car0 = Car(x0, y0, 90, self.blocks[checkpoint[0]][checkpoint[1]][0])
                car1 = Car(x1, y1, 270, self.blocks[checkpoint[0]][checkpoint[1]][0])
            elif neighbours == (False, False, True, True) \
                or neighbours == (False, False, True, False) \
                or neighbours == (False, False, False, True):
                car0 = Car(x0, y0, 0, self.blocks[checkpoint[0]][checkpoint[1]][0])
                car1 = Car(x1, y1, 180, self.blocks[checkpoint[0]][checkpoint[1]][0])
            self.blocks[checkpoint[0]][checkpoint[1]][3].append(car0)
            self.blocks[checkpoint[0]][checkpoint[1]][3].append(car1)


    
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
        count = 0
        for i in range(len(matrix)):
            blocks_line = []
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    blocks_line.append([count, pygame.Rect(x, y, block_width, block_height), constants.BLACK, []])
                elif matrix[i][j] == 1:
                    blocks_line.append([count, pygame.Rect(x, y, block_width, block_height), constants.WHITE, []])
                elif matrix[i][j] == 2:
                    blocks_line.append([count, pygame.Rect(x, y, block_width, block_height), constants.GRAY, []])
                    checkpoints.append((i, j))
                count += 1
                x += block_width
            blocks.append(blocks_line)
            x = 0
            y += block_height
        return City(blocks, checkpoints)
    
    def __str__(self):
        return "City={blocks=" + str(self.blocks) + ", checkpoints=" + str(self.checkpoints) + "}"
    
    def get_car_block(self, car):
        block_width = self.blocks[0][0][1].width
        block_height = self.blocks[0][0][1].height
        block_x_index = car.position[0] // block_width
        block_y_index = car.position[1] // block_height
        return (int(block_x_index), int(block_y_index))
    
    def display(self, screen):
        for i in range(len(self.blocks)):
            for j in range(len(self.blocks[i])):
                pygame.draw.rect(screen, self.blocks[i][j][2], self.blocks[i][j][1])
                car_to_keep = []
                for car_index in range(len(self.blocks[i][j][3])):
                    x, y = self.get_car_block(self.blocks[i][j][3][car_index])
                    if x != j or y != i:
                        self.blocks[y][x][3].append(self.blocks[i][j][3][car_index])
                    else:
                        car_to_keep.append(self.blocks[i][j][3][car_index])
                self.blocks[i][j][3] = car_to_keep
        
        for i in range(len(self.blocks)):
            for j in range(len(self.blocks[i])):
                for car_index in range(len(self.blocks[i][j][3])):
                    self.blocks[i][j][3][car_index].display(screen)
                    sub_blocks = []
                    for g in range(i - 1, i + 2):
                        sub_blocks.append(self.blocks[g][j - 1: j + 2])
                    self.blocks[i][j][3][car_index].move(sub_blocks)