colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

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

    for r in range(rows):
        q.append([])
        for c in range(cols):
            previousRow = (r - movementInRow) % rows
            previousCol = (c - movementInCol) % cols

            s = p_move * p[previousRow][previousCol] + (1-p_move) * p[r][c]

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









