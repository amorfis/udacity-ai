# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    current = [0, init[0], init[1]]
    openList = []
    openList.append(current)
    visited = []
    visited.append([current[1], current[2]])

    while current[1] != goal[0] or current[2] != goal[1]:
        visited.append([current[1], current[2]])
        possibilities = getPossibleNonVisitedMoves(current, openList, visited)

        withMinG = getNonVisitedPossibilityWithMinG(openList, visited)

        if withMinG == "none":
            return "fail"

        current = withMinG

    return current

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

def openListContains(openList, position):
    for openListItem in openList:
        if openListItem[1] == position[0] and openListItem[2] == position[1]:
            return 1

    return 0

print search()