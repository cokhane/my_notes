def twoloops(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


print(f"twoloops: {twoloops(5)}") 


'''
the first loop is i -> o(n)
the 2nd loop is j -> o(n)

o(n) + o(n) = o(2n) ( but sicne we ignore constant ) the total is still o(n )

'''