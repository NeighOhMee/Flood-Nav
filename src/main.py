'''
File: main.py

points are 38x18
roads are 37/8x35
length_map 37/8x35
'''

import ui
import navigation
import server
import grid

dimensions = (5, 5)
board = grid.grid([(1,0,2,0),(1,0,1,1),(1,1,2,1),(0,2,1,2)], (0,0), (5,5))
board.addFlooded((2, 0), (1, 1))
board.addFlooded((0, 2), (1, 1))
board.addFlooded((2, 2), (1, 1))
board.addFlooded((2, 1), (1, 2))
board.addFlooded((0, 1), (1, 2))
board.addFlooded((1, 0), (2, 1))

navigation.astar(board, (2, 0), (0, 0))

print("Startup...")
ui.startUp(dimensions, board)
server.startServer()