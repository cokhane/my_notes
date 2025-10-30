def axe(n):
    i = 0
    while i < n:
        j = 0
        while j < 3*n:
            j = j + 1
        j = 0
        while j < 2*n:
            j = j + 1
        i = i + 1

print(f"test: {axe(2)}")

'''
    f(n) = n * (3n +2n ) = 5n^2
    O(f(n)) = O(n^2)
'''


