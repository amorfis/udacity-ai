# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D() below.
#
# You are given a car in a grid with initial state
# init = [x-position, y-position, orientation]
# where x/y-position is its position in a given
# grid and orientation is 0-3 corresponding to 'up',
# 'left', 'down' or 'right'.
#
# Your task is to compute and return the car's optimal
# path to the position specified in `goal'; where
# the costs for each motion are as defined in `cost'.

# EXAMPLE INPUT:

# grid format:
#     0 = navigable space
#     1 = occupied space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]
goal = [2, 0] # final position
init = [4, 3, 0] # first 2 elements are coordinates, third is direction
cost = [2, 1, 20] # the cost field has 3 values: right turn, no turn, left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D() should return the array
# 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
#
# ----------


# there are four motion directions: up/left/down/right
# increasing the index in this array corresponds to
# a left turn. Decreasing is is a right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # do right
forward_name = ['up', 'left', 'down', 'right']

# the cost field has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']


# ----------------------------------------
# modify code below
# ----------------------------------------

#def compute_next_steps(current):
#    next_steps = []
#    orientation = current[2]
#
#    for i in range(len(action)):
#        new_orientation = orientation + action[i]
#        new_orientation = new_orientation % len(forward)
#        move = forward[new_orientation]
#
#        next_step = [current[0] + move[0], current[1] + move[1], new_orientation, current[3] + cost[i]]
#
#        #Check off board
#        if next_step[0] < 0 or next_step[0] >= len(grid) or next_step[1] < 0 or next_step[1] >= len(grid[0]):
#            continue
#
#        #Check if already visited
##        if visited[next_step[0]][next_step[1]]:
##            continue
#
#        #Check for obstacle
#        if grid[next_step[0]][next_step[1]] == 1:
#            continue
#
#        next_steps.append(next_step)
#
#    return next_steps

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

#def optimum_policy():
#
#
#    movesGrid = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
#
#    for r in range(len(grid)):
#        for c in range(len(grid[r])):
#            if grid[r][c] == 1:
#                continue
#
#            start = [r, c]
#            fill_in_grid_from(start, movesGrid, distances)
#
#    movesGrid[goal[0]][goal[1]] = '*'
#
#    return distances






#--------------------------------
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



def get_possible_non_visited_moves(current, openList, visited, distances):
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


def compute_value(path_goal):
    output = [[[999 for col in range(len(grid[0]))] for row in range(len(grid))] for theta in range(4)]


#    for i in range(len(output)):
#        print "Theta: " + str(i)
#        for row in output[i]:
#            print row


    possible_prev_steps = []
    for i in range(4):
        possible_prev_steps.append([path_goal[0], path_goal[1], i, 0])
    changed = True
    while changed:
        possible_prev_steps_for_next_iter = []
        changed = False
        for current in possible_prev_steps:
            old_value = output[current[2]][current[0]][current[1]]
            if old_value > current[3]:
                output[current[2]][current[0]][current[1]] = current[3]
                changed = True

            possible_prev_steps_for_next_iter.extend(compute_possible_prev_steps(current))

        possible_prev_steps = possible_prev_steps_for_next_iter

    return output


def compute_possible_prev_steps(current):
    prev_steps = []
    orientation = current[2]

    for i in range(len(action)):
        prev_orientation = orientation - action[i]
        prev_orientation = prev_orientation % len(forward)

        #move was made with current orientation. Orientation is changed first when moving, then the move is actioned
        move = forward[orientation]

        prev_step = [current[0] - move[0], current[1] - move[1], prev_orientation, current[3] + cost[i]]

        #Check off board
        if prev_step[0] < 0 or prev_step[0] >= len(grid) or prev_step[1] < 0 or prev_step[1] >= len(grid[0]):
            continue

#        Check if already visited
#        if visited[prev_step[2]][prev_step[0]][prev_step[1]]:
#            continue

        #Check for obstacle
        if grid[prev_step[0]][prev_step[1]] == 1:
            continue

        prev_steps.append(prev_step)

    return prev_steps

def optimum_policy2D():
    return compute_value(goal)

matrix = optimum_policy2D()
for t in range(len(matrix)):
    theta_matrix = matrix[t]
    print "Theta " + str(t)
    for row in theta_matrix:
        print row
