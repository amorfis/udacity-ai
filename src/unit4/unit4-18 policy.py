# ----------
# User Instructions:
# 
# Create a function optimum_policy() that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell.
# 
# un-navigable cells must contain an empty string
# WITH a space, as shown in the previous video.
# Don't forget to mark the goal with a '*'

# ----------

grid = [[0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# modify code below
# ----------------------------------------

def compute_value():
    visited = [[False for row in range(len(grid[0]))] for col in range(len(grid))]
    output = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]

    next_steps = []
    next_steps.append([goal[0], goal[1], 0])
    while len(next_steps) > 0:
        next_steps_for_next_iter = []
        for current in next_steps:
            output[current[0]][current[1]] = current[2]
            visited[current[0]][current[1]] = True

            next_steps_for_next_iter.extend(compute_next_steps(current, visited))

        next_steps = next_steps_for_next_iter

    return output

def compute_next_steps(current, visited):
    next_steps = []
    for d in delta:
        next_step = [current[0] + d[0], current[1] + d[1], current[2] + cost_step]

        #Check off board
        if next_step[0] < 0 or next_step[0] >= len(grid) or next_step[1] < 0 or next_step[1] >= len(grid[0]):
            continue

        #Check if already visited
        if visited[next_step[0]][next_step[1]]:
            continue

        #Check for obstacle
        if grid[next_step[0]][next_step[1]] == 1:
            continue

        next_steps.append(next_step)

    return next_steps

def getMoveName(prev, current):
    for i in range(len(delta)):
        currentDelta = delta[i]
        prevPlusDelta = [prev[0] + currentDelta[0], prev[1] + currentDelta[1]]
        if prevPlusDelta == current:
            return delta_name[i]


def addToListOnPosition(list, entry, position):
    while(len(list) < position+1):
        list.append(0)

    list[position] = entry

def already_on_grid(movesGrid, position):
    return movesGrid[position[0]][position[1]] != ' '

def fill_in_grid_from(current, movesGrid, distances):
    current_position = current

    current = [0, current[0], current[1]]
    openList = []
    openList.append(current)

    visited = []

    moves = [current_position]

    step = 0
    goal_reached = True
    while current_position[0] != goal[0] or current_position[1] != goal[1]:
        visited.append(current_position)
        getPossibleNonVisitedMoves(current, openList, visited, distances)

        current = getNonVisitedPossibilityWithMinF(openList, visited)
        current_position = [current[1], current[2]]

        if current == "none":
            goal_reached = False
            break

        addToListOnPosition(moves, current_position, current[0])
        if already_on_grid(movesGrid, current_position):
            break

        step += 1

    if goal_reached:
        for i in range(1, len(moves)):
            prev = moves[i-1]
            current = moves[i]

            name = getMoveName(prev, current)
            movesGrid[prev[0]][prev[1]] = name

def getNonVisitedPossibilityWithMinF(possibilities, visited):
    min = "none"
    for current in possibilities:
        if [current[1], current[2]] in visited:
            continue
        if min == "none" or current[3] < min[3]:
            min = current

    return min

def getPossibleNonVisitedMoves(current, openList, visited, distances):
    possibilities = []
    for move in delta:
        possibility = [current[1] + move[0], current[2] + move[1]]

        x = possibility[1]
        y = possibility[0]
        #Remove if off grid
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
            continue
        #Remove if already visited
        if [possibility[0], possibility[1]] in visited:
            continue
        #Remove if on obstacle
        if grid[y][x] == 1:
            continue

        possibilities.append(possibility)

    for possibility in possibilities:
        x = possibility[1]
        y = possibility[0]
        openList.append([current[0] + cost_step, y, x, current[0] + distances[y][x]])

    return possibilities



def optimum_policy():
    distances = compute_value()

    print "Distances:"
    for row in distances:
        print row

    movesGrid = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                continue

            start = [r, c]
            fill_in_grid_from(start, movesGrid, distances)

    movesGrid[goal[0]][goal[1]] = '*'

    return movesGrid

def compute_value2():
    visited = [[False for row in range(len(grid[0]))] for col in range(len(grid))]
    output = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]

    next_steps = []
    next_steps.append(goal)
    distance_counter = 0
    while len(next_steps) > 0:
        next_steps_for_next_iter = []
        for current in next_steps:
            output[current[0]][current[1]] = distance_counter
            visited[current[0]][current[1]] = True

            next_steps_for_next_iter.extend(compute_next_steps(current, visited))

        distance_counter += 1
        next_steps = next_steps_for_next_iter

    return output

for row in optimum_policy():
    print row


