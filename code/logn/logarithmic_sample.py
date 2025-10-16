import math

def logFunc(n):
    if n == 0:
        return "Done"
    n = math.floor(n/2)
    print(n)
    return logFunc(n)

### O ( log n ) non recursive 

def logn(n):
    while n > 1:
        n = math.floor(n/2)
        print(n)


print(logn(8))