def f(n):
    if n == 0:
        print("*******")
        return
    
    print(f"this is N:{n}")
    for i in range(n):
        f(n-1)



print(f(3))
        