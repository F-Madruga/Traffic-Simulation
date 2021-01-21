# Generate Blocks for the city
#

import pygame

# Pygame used for visualisation
# and for enviormnent


def read_block(_file="Exemplos/cruzamento.txt"):
    """
    Reads blocks from text files
    and returns an array representation.
    """
    block = open(_file, "r")
    lines = block.readlines()

    city_block = []
    for line in lines:
        city_block.append(list(line[:-1]))

    block.close()
    return city_block


def block_gen(inp=None, scale=100,
              size=(5, 5), _type="inter"):
    """
    Generates a city block
    """
    block = []
    if inp is None:
        print("empty input")
    else:
        size = (len(inp[0])*scale, len(inp)*scale)
        if _type == "inter":

            h = inp[0].index("1") * scale
            v = 0
            r = 1 * scale
            for i, l in enumerate(inp):
                if "0" not in l:
                    v = i * scale

            print(h)
            print(v)
            print(r)
            print(size)

            p1 = [h, 0]
            p2 = [h, v]
            p1_t = [h + r, 0]
            p2_t = [h + r, v]
            block.append((p1, p2))
            block.append((p1_t, p2_t))

            p1 = [0, v]
            p2 = [h, v]
            p1_t = [0, v + r]
            p2_t = [h, v + r]
            block.append((p1, p2))
            block.append((p1_t, p2_t))

            p1 = [h, v + r]
            p2 = [h, size[1]]
            p1_t = [h + r, v + r]
            p2_t = [h + r, size[1]]
            block.append((p1, p2))
            block.append((p1_t, p2_t))

            p1 = [h + r, v + r]
            p2 = [size[0], v + r]
            p1_t = [h + r, v]
            p2_t = [size[0], v]
            block.append((p1, p2))
            block.append((p1_t, p2_t))

            block.append(size)

    return block


def display(block):
    """
    Display the city in pygame
    """
    carryOn = True
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    pygame.init()
    screen = pygame.display.set_mode(block[-1])
    pygame.display.set_caption("City Display")

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False

        screen.fill(BLACK)
        for line in block[:-1]:
            pygame.draw.line(screen, WHITE,
                             line[0], line[1], 2)
        pygame.display.update()
    pass
