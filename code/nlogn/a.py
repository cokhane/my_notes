import math 

def nLogNFunc(n): 
    y = n 
    while n > 1:
        n = math.floor(n/2)
        for i in range(y):
            print(i)

print(nLogNFunc(10))
