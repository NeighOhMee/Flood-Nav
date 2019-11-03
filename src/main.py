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
import flood

dimensions = (10, 10)
board = grid.grid([], (0,0), dimensions)
flood.generateFloods(board)
start_end = flood.generateGoal(dimensions)

print("Start / Goal:", start_end[0], start_end[1])
path = navigation.astar(board, start_end[0], start_end[1])

print("Startup...")
ui.startUp(dimensions, board, start_end)
server.startServer(len(path), len(path))