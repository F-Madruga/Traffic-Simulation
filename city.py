import pygame
import constants

class City():
    def __init__(self, matrix):
        self.matrix = matrix
    
    @staticmethod
    def read_file(path):
        matrix = []
        file = open(path, "r")
        lines = file.readlines()
        for line in lines:
            matrix_line = []
            for cell in line:
                if cell == "0" or cell == "1":
                    matrix_line.append(int(cell))
            matrix.append(matrix_line)
        return City(matrix)
    
    def __str__(self):
        return "City={" + str(self.matrix) + "}"
    
    def display(self, screen):
        screen_width, screen_height = screen.get_size()
        block_width = screen_width / len(self.matrix[0])
        block_height = screen_height / len(self.matrix)
        x = 0
        y = 0
        for line in self.matrix:
            for cell in line:
                if cell == 0:
                    pygame.draw.rect(screen, constants.BLACK, pygame.Rect(x, y, block_width, block_height))
                else:
                    pygame.draw.rect(screen, constants.WHITE, pygame.Rect(x, y, block_width, block_height))
                x += block_width
            x = 0
            y += block_height