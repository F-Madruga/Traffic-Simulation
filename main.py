import sys
import pygame
import constants
from city import City


def main(argv):

    city = City.read_file(argv[0], constants.WIDTH, constants.HEIGHT)

    carryOn = True
    pygame.init()
    size = (constants.WIDTH, constants.HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Traffic Simulator")
    while carryOn:
        screen.fill(constants.BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT \
                    or event.key == pygame.K_DOWN) \
                    and constants.VELOCITY - 0.01 > 0:
                    constants.VELOCITY -= 0.01
                if (event.key == pygame.K_RIGHT \
                    or event.key == pygame.K_UP) \
                    and constants.VELOCITY + 0.01 < 4:
                    constants.VELOCITY += 0.01
        city.display(screen)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    argv = sys.argv[1:]
    if len(argv) == 0:
        argv.append("./examples/city_1.txt")
    main(argv)