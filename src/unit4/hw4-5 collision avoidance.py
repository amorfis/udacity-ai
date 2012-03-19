# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# takes no input and RETURNS two grids. The
# first grid, value, should contain the computed
# value of each cell as shown in the video. The
# second grid, policy, should contain the optimum
# policy for each cell.
#
# Stay tuned for a homework help video! This should
# be available by Thursday and will be visible
# in the course content tab.
#
# Good luck! Keep learning!
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.
#
# NOTE: Please do not modify the values of grid,
# success_prob, collision_cost, or cost_step inside
# your function. Doing so could result in your
# submission being inappropriately marked as incorrect.

# -------------
# GLOBAL VARIABLES
#
# You may modify these variables for testing
# purposes, but you should only modify them here.
# Do NOT modify them inside your stochastic_value
# function.

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]

goal = [0, len(grid[0])-1] # Goal is in top right corner


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

success_prob = 0.5
failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
collision_cost = 100                    
cost_step = 1        
                     

############## INSERT/MODIFY YOUR CODE BELOW ##################
#
# You may modify the code below if you want, but remember that
# your function must...
#
# 1) ...be called stochastic_value().
# 2) ...NOT take any arguments.
# 3) ...return two grids: FIRST value and THEN policy.

def is_colliding(position):
    x = position[0]
    y = position[1]

    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return True

    if grid[x][y] == 1:
        return True

    return False

def get_value(position, values):
    if is_colliding(position):
        return collision_cost

    return values[position[0]][position[1]]

def stochastic_value():
    value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    value[goal[0]][goal[1]] = 0
    policy[goal[0]][goal[1]] = '*'

    change = True
    while change:
        change = False
        for x in range(len(value)):
            for y in range(len(value[0])):
                if is_colliding([x, y]):
                    continue

                for i in range(len(delta)):
                    move = delta[i]
                    sidestep1delta = delta[(i - 1) % len(delta)]
                    sidestep2delta = delta[(i + 1) % len(delta)]

                    main_move = [x + move[0], y + move[1]]
                    if is_colliding(main_move):
                        continue

                    sidestep1 = [x + sidestep1delta[0], y + sidestep1delta[1]]
                    sidestep2 = [x + sidestep2delta[0], y + sidestep2delta[1]]

                    new_value = get_value(main_move, value) * success_prob
                    new_value += get_value(sidestep1, value) * failure_prob
                    new_value += get_value(sidestep2, value) * failure_prob
                    new_value += cost_step

                    old_value = get_value([x, y], value)
                    if new_value < old_value:
                        value[x][y] = new_value
                        policy[x][y] = delta_name[i]
                        change = True
    
    return value, policy

