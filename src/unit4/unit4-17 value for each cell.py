# ----------
# User Instructions:
#
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal.
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
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
# insert code below
# ----------------------------------------

def compute_value():
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

def compute_next_steps(current, visited):
    next_steps = []
    for d in delta:
        next_step = [current[0] + d[0], current[1] + d[1]]

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

for row in compute_value():
    print row