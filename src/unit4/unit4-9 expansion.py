# -----------
# User Instructions:
#
# Modify the function search() so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# For grading purposes, please leave the return
# statement at the bottom.
# ----------


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

    expand[0][0] = 0
    step = 0
    while current[1] != goal[0] or current[2] != goal[1]:
        visited.append([current[1], current[2]])
        possibilities = getPossibleNonVisitedMoves(current, openList, visited)

        current = getNonVisitedPossibilityWithMinG(openList, visited)

        if current == "none":
            break

        step += 1
        expand[current[1]][current[2]] = step

    return expand

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

for row in search():
    print row