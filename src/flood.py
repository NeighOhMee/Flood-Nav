import random

FLOOD_ZONES = 15
ZONE_SIZE = 5
RAND_FLOOD = 3

def generateFloods(board):
    for i in range(FLOOD_ZONES):
        start = [random.randrange(0, board.bound[1][0]), random.randrange(0, board.bound[1][1])]
        for j in range(3):
            curr_point = [start[0], start[1]]
            for k in range(ZONE_SIZE):
                direction = random.choice([(-1, 1), (1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1)])
                board.addFlooded((curr_point[0], curr_point[1]), (curr_point[0]+direction[0], curr_point[1]+direction[1]))
                curr_point[0] += direction[0]
                curr_point[1] += direction[1]
    for i in range(RAND_FLOOD):
        curr_point = (random.randrange(0, board.bound[1][0]), random.randrange(0, board.bound[1][1]))
        direction = random.choice([(-1, 1), (1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1)])
        board.addFlooded((curr_point[0], curr_point[1]), (curr_point[0]+direction[0], curr_point[1]+direction[1]))

def generateGoal(dimensions):
    return ((random.randrange(0, dimensions[0]), random.randrange(0, dimensions[1])), (random.randrange(0, dimensions[0]), random.randrange(0, dimensions[1])))