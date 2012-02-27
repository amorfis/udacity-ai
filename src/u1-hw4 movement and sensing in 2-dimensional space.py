colors = [['green', 'green', 'green'],
          ['green', 'red', 'red'],
          ['green', 'green', 'green']]

measurements = ['red', 'red']

motions = [[0,0], [0,1]]

sensor_right = 1

p_move = 0.5

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p = []

rows = len(colors)
cols = len(colors[0])
uniform = 1.0 / (rows * cols)
sensor_wrong = 1 - sensor_right

for r in range(rows):
    p.append([])
    for c in range(cols):
        p[r].append(uniform)

def sense(p, Z):
    q=[]
    for r in range(rows):
        q.append([])
        for c in range(cols):
            isMatched = Z == colors[r][c]
            senseValue = isMatched * sensor_right + (1-isMatched) * sensor_wrong
            q[r].append(p[r][c] * senseValue)

    return normalize(q)

def move(p, U):
    q = []
    movementInRow = U[0]
    movementInCol = U[1]

    temp_p_move = p_move

    if abs(movementInRow) + abs(movementInCol) == 0:
        temp_p_move = 1

    for r in range(rows):
        q.append([])
        for c in range(cols):
            p_wrongMove = (1 - temp_p_move) / 2 * (abs(movementInRow) + abs(movementInCol))

            previousRow = (r - movementInRow) % rows
            previousCol = (c - movementInCol) % cols

            s = temp_p_move * p[previousRow][previousCol]
            s += p_wrongMove * p[(previousRow - 1) % rows][previousCol] * abs(movementInRow)
            s += p_wrongMove * p[(previousRow + 1) % rows][previousCol] * abs(movementInRow)
            s += p_wrongMove * p[previousRow][(previousCol - 1) % cols] * abs(movementInCol)
            s += p_wrongMove * p[previousRow][(previousCol + 1) % cols] * abs(movementInCol)

            sumProb = temp_p_move + p_wrongMove * abs(movementInRow) * 2 + p_wrongMove * abs(movementInCol) * 2
            print sumProb

            q[r].append(s)

    return normalize(q)

def normalize(p):
    s = 0
    for l in range(len(p)):
        s += sum(p[l])

    for r in range(rows):
        for c in range(cols):
            p[r][c] /= s

    return p

for i in range(len(measurements)):
    p = move(p, motions[i])
    p = sense(p, measurements[i])





#Your probability array must be printed
#with the following code.

show(p)









