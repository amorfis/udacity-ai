#Write a program that will find the initial number
#of coconuts. 

def f(n):
    return (n-1) / 5 * 4

def f6(n):
    for i in range(6):
        n = f(n)
    return n 

def is_int(n):
    return abs(n-int(n)) < 0.0000001
   
# Enter code here.
for i in range(20000):
    final = f6(i/1.)
    if (is_int(final)):
        n = i
        break

print n
