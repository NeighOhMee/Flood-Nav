'''
File: ui.py

This module controls the pygames output interface
'''

import pygame

def startUp():
    done = True

def shutDown():
    done = False

def drawRect(screen, color, position, size):
    pygame.draw.rect(screen, color, pygame.Rect(position[0], position[1], size[0], size[1]))

pygame.init()
myfont = pygame.font.SysFont('bahnschrift', 50)
screen = pygame.display.set_mode((1485, 685))
done = False
clock = pygame.time.Clock()
board = []

for i in range(35):
        if i % 2 == 0:
            board.append([0]*37)
        else:
            board.append([0]*38)

board[3][0] = 1
board[2][0] = 1
board[3][1] = 1
board[1][2] = 1

while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
    screen.fill((194, 210, 180))
    pressed = pygame.key.get_pressed()
    for i in range(38):
        for j in range(18):
            drawRect(screen, (0, 0, 0), (i*40, j*40), (5, 5))
    for i in range(35):
        if i % 2 == 0:
            j_range = 37
        else:
            j_range = 38
        for j in range(j_range):
            if board[i][j] == 1:
                color = (0, 153, 255)
            elif board[i][j] == 2:
                color = (255, 0, 0)
            else:
                color = (0, 255, 0)
            if i % 2 == 0: drawRect(screen, color, ((j)*40+5, (i//2)*40+1), (35, 3))
            if i % 2 == 1: drawRect(screen, color, ((j)*40+1, (i//2)*40+5), (3, 35))
    clock.tick()
    pygame.display.flip()    
pygame.quit()