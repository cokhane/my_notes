def axe(n):
    i = 0
    while i < 3 * n:
        j = 10
        while j < 50:
            j = j + 1
        j = 0
        while j < n*n*n:
            j = j + 2
        i = i + 1

print(f"test: {axe(2)}")

'''
    f(n) = 3n * 40 + n^3/2 ) = 3n/40 + 3n^4/2
     O(f(n)) = O(n^4)
'''


