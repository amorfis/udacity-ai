#Program a function that returns a new distribution 
#q, shifted to the right by U units. If U=0, q should 
#be the same as p.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q=[0]*len(p) #q should be by default initialized by zeroes
    for i, pre in enumerate(p):
        prob = p[(i - U) % len(p)]
        q[i] = q[i] + prob * pExact

        undershot = (i-1) % len(q)
        overshot = (i+1) % len(q)

        q[undershot] = q[undershot] + prob * pUndershoot
        q[overshot] = q[overshot] + prob * pOvershoot

    return q

for i in range(1000):
    p = move(p, 1)

print p