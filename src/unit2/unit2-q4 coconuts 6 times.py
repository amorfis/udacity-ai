#Write a function that takes the number of 
#coconuts, n, as an argument and returns the
#number of coconuts after one is given to
#the monkey and one fifth are taken away.


def f(n):
    afterMonkey = n-1

    return 4*afterMonkey / 5.

def f6(n):
    for i in range(6):
        n = f(n)

    return n

print f6(96.)
