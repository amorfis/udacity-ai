# ----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,
# up, and down motions. NOTE: the 'v' should be
# lowercase.
#
# Your function should be able to do this for any
# provided grid, not just the sample grid below.
# ----------


# Sample Test case
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

# ----------------------------------------
# modify code below
# ----------------------------------------

def search():
    current = [0, init[0], init[1]]
    openList = []
    openList.append(current)
    visited = []
    visited.append([current[1], current[2]])
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    moves = []

    expand[0][0] = 0
    step = 0
    while current[1] != goal[0] or current[2] != goal[1]:
        visited.append([current[1], current[2]])
        getPossibleNonVisitedMoves(current, openList, visited)

        current = getNonVisitedPossibilityWithMinG(openList, visited)

        if current == "none":
            break

        addToMoves(moves, current)

        step += 1
        expand[current[1]][current[2]] = step

    movesGrid = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    for i in range(1, len(moves)):
        prev = moves[i-1]
        current = moves[i]

        name = getMoveName(prev, current)
        movesGrid[prev[0]][prev[1]] = name

    lastMove = moves[-1]
    movesGrid[lastMove[0]][lastMove[1]] = '*'

    return movesGrid

def getMoveName(prev, current):
    for i in range(len(delta)):
        currentDelta = delta[i]
        prevPlusDelta = [prev[0] + currentDelta[0], prev[1] + currentDelta[1]]
        if prevPlusDelta == current:
            return delta_name[i]


def addToMoves(moves, positionWithG):
    g = positionWithG[0]
    while(len(moves) < g+1):
        moves.append([0, 0])

    moves[g] = [positionWithG[1], positionWithG[2]]

def getNonVisitedPossibilityWithMinG(possibilities, visited):
    min = "none"
    for current in possibilities:
        if [current[1], current[2]] in visited:
            continue
        if min == "none" or current[0] < min[0]:
            min = current

    return min


def getPossibleNonVisitedMoves(current, openList, visited):
    possibilities = []
    for move in delta:
        possibilities.append([current[1] + move[0], current[2] + move[1]])

    toRemove = []
    for possibility in possibilities:
        x = possibility[1]
        y = possibility[0]
        #Remove if off grid
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
            toRemove.append(possibility)
            continue
        #Remove if already visited
        if [possibility[0], possibility[1]] in visited:
            toRemove.append(possibility)
            continue
        #Remove if on obstacle
        if grid[y][x] == 1:
            toRemove.append(possibility)
            continue

    for x in toRemove:
        possibilities.remove(x)

    for possibility in possibilities:
        openList.append([current[0] + cost, possibility[0], possibility[1]])

    return possibilities
