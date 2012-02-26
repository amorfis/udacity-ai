#Modify the code so that it updates the probability twice
#and gives the posterior distribution after both 
#measurements are incorporated. Make sure that your code 
#allows for any sequence of measurement of any length.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, mesaurement):
    q=[]
    for i, prob in enumerate(p):
        hit = (mesaurement == world[i])
        multiplier = (hit * pHit + (1 - hit) * pMiss)
        prob = prob * multiplier

        q.append(prob)

    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s

    return q

for i in range(2):
    p = sense(p, measurements[i])
    
print sense(p, measurements)
