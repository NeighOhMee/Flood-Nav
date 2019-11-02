'''
File: ui.py

This module controls the pygames output interface
'''

import pygame

def startUp(dimensions, grid):
    dimensions = dimensions
    board = grid
    done = True

def shutDown():
    done = False

def drawRect(screen, color, position, size):
    pygame.draw.rect(screen, color, pygame.Rect(position[0], position[1], size[0], size[1]))

pygame.init()
dimensions = (3, 3)
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
            drawRect(screen, (0, 0, 0), (i*40, j*40), (5, 5))
    
    clock.tick()
    pygame.display.flip()    
pygame.quit()