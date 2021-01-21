# City Builder
import pygame

from Car import Car

clock = pygame.time.Clock()
carryOn = True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Traffic Simulator")

car1 = Car(225,10)

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
    screen.fill(BLACK)
    #pygame.draw.line(screen, WHITE, [200, 0], [200, 200], 2)
    #pygame.draw.line(screen, WHITE, [300, 0], [300, 200], 2)
    #pygame.draw.line(screen, WHITE, [0, 200], [200, 200], 2)
    #pygame.draw.line(screen, WHITE, [0, 300], [200, 300], 2)
    #pygame.draw.line(screen, WHITE, [200, 300], [200, 500], 2)
    #pygame.draw.line(screen, WHITE, [300, 300], [300, 500], 2)
    #pygame.draw.line(screen, WHITE, [300, 200], [500, 200], 2)
    #pygame.draw.line(screen, WHITE, [300, 300], [500, 300], 2)


    car1.move_down()
    car1.display(screen)
    pygame.display.update()
pygame.quit()
