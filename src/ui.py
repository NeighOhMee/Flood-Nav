'''
File: ui.py

This module controls the pygames output interface
'''

import pygame
import grid

def startUp(dimensions, grid):
    dimensions = dimensions
    board = grid
    done = True

def shutDown():
    done = False

def drawRect(screen, color, position, size):
    pygame.draw.rect(screen, color, pygame.Rect(position[0], position[1], size[0], size[1]))

pygame.init()
dimensions = (32, 32)
board = grid.grid([(1,0,2,0),(1,0,1,1),(1,1,2,1),(0,2,1,2)], (0,0), (32,17))
board.addFlooded((2, 0), (1, 1))
board.addFlooded((0, 2), (1, 1))
board.addFlooded((2, 2), (1, 1))
myfont = pygame.font.SysFont('bahnschrift', 50)
screen = pygame.display.set_mode(((dimensions[0]-1)*40+5, (dimensions[1]-1)*40+5))
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
    screen.fill((194, 210, 180))
    pressed = pygame.key.get_pressed()
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            for direction in [(0, 1), (1, 0), (1, 1)]:
                connection_status = board.checkConnection((i, j), (i+direction[0], j+direction[1]))
                if connection_status < 2:
                    if connection_status == 0:
                        color = (0, 255, 0)
                    else:
                        color = (0, 153, 255)
                    if direction[0] and not direction[1]:
                        drawRect(screen, color, (j*40+1, i*40+5), (3, 40))
                    elif not direction[0] and direction[1]:
                        drawRect(screen, color, (j*40+5, i*40+1), (40, 3))
                    else:
                        pygame.draw.polygon(screen, color, [(j+5, i+4), (j+4, i+5), (j+45), (i+45)], 0)

    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            drawRect(screen, (0, 0, 0), (i*40, j*40), (5, 5))
    clock.tick()
    pygame.display.flip()

dirname = os.path.dirname(__file__)
full_path = os.path.join(dirname, 'static/images/screenshot.png')
pygame.image.save( screen, full_path)    
pygame.quit()