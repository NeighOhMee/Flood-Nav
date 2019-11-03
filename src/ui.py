'''
File: ui.py

This module controls the pygames output interface
'''

import pygame
import grid
import os

def drawRect(screen, color, position, size):
    pygame.draw.rect(screen, color, pygame.Rect(position[0], position[1], size[0], size[1]))

def startUp(dimensions, grid):
    board = grid
    pygame.init()
    screen = pygame.display.set_mode(((dimensions[1]-1)*40+5, (dimensions[0]-1)*40+5))
    done = False
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            for direction in [(0, 1), (1, 0), (1, 1), (-1, 1)]:
                connection_status = board.checkConnection((i, j), (i+direction[0], j+direction[1]))
                if connection_status != 2:
                    if connection_status == 0:
                        color = (177, 181, 184)
                    elif connection_status == 1:
                        color = (0, 153, 255)
                    else:
                        color = (68, 190, 80)
                    if direction[0] and not direction[1]:
                        drawRect(screen, color, (j*40+1, i*40+5), (3, 40))
                    elif not direction[0] and direction[1]:
                        drawRect(screen, color, (j*40+5, i*40+1), (40, 3))
                    elif direction[0] > 0:
                        pygame.draw.polygon(screen, color, [(j*40+5, i*40+2), (j*40+2, i*40+5), (j*40+45, i*40+48), (j*40+48, i*40+45)], 0)
                    else:
                        pygame.draw.polygon(screen, color, [(j*40+1, i*40), (j*40+5, i*40+2), (j*40+42, i*40-35), (j*40+40, i*40-39)], 0)
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            drawRect(screen, (0, 0, 0), (j*40, i*40), (5, 5))
    clock.tick()
    dirname = os.path.dirname(__file__)
    full_path = os.path.join(dirname, 'static/images/screenshot.png')
    pygame.image.save( screen, full_path)    
    pygame.quit()
    done = True

def shutDown():
    done = False