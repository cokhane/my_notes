def countdown(n):
    if n == 0:
        return 

    print(f"n: {n}")
    return countdown(n-1)


print(f"countdown: {countdown(3)}")