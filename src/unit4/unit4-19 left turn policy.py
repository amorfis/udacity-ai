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

def compute_to_goal(path_goal):
    visited = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))] for theta in range(4)]
    output = [[[999 for col in range(len(grid[0]))] for row in range(len(grid))] for theta in range(4)]

    possible_prev_steps = []
    for i in range(4):
        possible_prev_steps.append([path_goal[0], path_goal[1], i, 0])
    while len(possible_prev_steps) > 0:
        possible_prev_steps_for_next_iter = []
        for current in possible_prev_steps:
            old_value = output[current[2]][current[0]][current[1]]
            if old_value > current[3]:
                output[current[2]][current[0]][current[1]] = current[3]

            possible_prev_steps_for_next_iter.extend(compute_possible_prev_steps(current, visited))

        possible_prev_steps = possible_prev_steps_for_next_iter

    return output


def compute_possible_prev_steps(current, visited):
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
        visited_value = visited[prev_step[2]][prev_step[0]][prev_step[1]]
        if visited_value <= prev_step[3]:
            continue

        #Check for obstacle
        if grid[prev_step[0]][prev_step[1]] == 1:
            continue

        prev_steps.append(prev_step)

    return prev_steps


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

def get_non_visited_possibility_with_min_distance(possibilities, visited):
    min = "none"
    for current in possibilities:
        if [current[1], current[2]] in visited:
            continue
        if min == "none" or current[3] < min[3]:
            min = current

    return min

def get_possible_moves_with_names(current):
    possibilities = []

    for i in range(len(action)):
        next_orientation = current[2] + action[i]
        next_orientation = next_orientation % len(forward)

        #move was made with current orientation. Orientation is changed first when moving, then the move is actioned
        move = forward[next_orientation]

        next_step = [current[0] + move[0], current[1] + move[1], next_orientation, current[3] + cost[i]]

        #Check off board
        if next_step[0] < 0 or next_step[0] >= len(grid) or next_step[1] < 0 or next_step[1] >= len(grid[0]):
            continue

        #Check for obstacle
        if grid[next_step[0]][next_step[1]] == 1:
            continue

        possibilities.append([next_step, action_name[i]])

    return possibilities


def get_next_move_with_name(current, distances):
    possibilities = get_possible_moves_with_names(current)

    if len(possibilities) == 0:
        return "fail"

    optimal_with_name = possibilities[0]
    for possibility in possibilities:
        current_optimal = optimal_with_name[0]
        possible_move = possibility[0]

        g_for_current_optimal = distances[current_optimal[2]][current_optimal[0]][current_optimal[1]] + current_optimal[3]
        g_for_possibility = distances[possible_move[2]][possible_move[0]][possible_move[1]] + possible_move[3]

        if g_for_possibility < g_for_current_optimal:
            optimal_with_name = possibility

    return optimal_with_name

def fill_in_grid_from(current, moves_grid, distances):
    current = [current[0], current[1], current[2], 0]
    while current[0] != goal[0] or current[1] != goal[1]:
        next_with_name = get_next_move_with_name(current, distances)

        name = next_with_name[1]

        moves_grid[current[0]][current[1]] = name

        current = next_with_name[0]

    moves_grid[current[0]][current[1]] = "*"

def optimum_policy2D():
    costs = compute_to_goal(goal)

    for t in range(len(costs)):
        theta_matrix = costs[t]
        print "Theta " + str(t)
        for row in theta_matrix:
            print row
    print

    moves = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    fill_in_grid_from(init, moves, costs)

    return moves

for row in optimum_policy2D():
    print row
