def sixthStep(x):
    firstStep = 5*x+1
    ff=5./4.
    f = ff*ff*ff*ff*ff * firstStep + ff*ff*ff*ff + ff*ff*ff + ff*ff + ff + 1

    return f

for x in range(10000):
    f = sixthStep(x)
    if (f % 5 == 1):
        print str(x) + ": " + str(f)



