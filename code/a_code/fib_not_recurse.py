'''
how to get n of fibonachi 

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
a  b  c
   a  b  c
      a  b  c 

'''


def fib(n):
    a = 0
    b = 1
    c = 0
    for i in range(n):
       print(a)
       c = a + b
       a, b = b,c


print(fib(5))
    