

# class Solutions():

#     def multiply(self, c: int, d: int) -> int:
#         return self.add(c,d) * 2 

#     def add(self, a: int, b: int) -> int:
#         return a + b
    
#     def nested_list(self, test_list):
#         return [self.add(self.multiply(i,2),1) for i in test_list]
    
#     def ternary_else_if(self, test_list):
#         return [self.add(i,1) if i%2==0 else self.multiply(i,2) for i in test_list]
    
#     def ternary_if(self, test_list):
#         return [self.add(n,n+1) for n in test_list if n % 2 == 0]

# x = Solutions()
# print(x.ternary_if([2,3,5,6]))

'''

given an integer n, 

"Axe" if i is divisible by 3 and 5,
"Paul" if i is divisible by 3,
"Russel" if i is divisible by 5
check i if its a prime number, 
return P for prime, NP, for not prime

Input: n = 3
Output: ["NP:1", "P:2", "Paul"]

Input: n = 10
Output: ["NP:1", "P:2", "Paul", "NP:4", "Russel", "Paul", "P:7", "NP:8", "Paul", "Russel"]

Input: n = 15
Output: ["NP:1", "P:2", "Paul", "NP:4", "Russel", "Paul", "P:7", "NP:8", "Paul", "Russel", P:11", "Paul","P:13", "NP:14", "axe"]

Note; no need to put it in a list, you can just print it out as a long as the sequence is correct 

sample prime number: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53


#Use this boilerplate

class Solutions():
    def leomar(self, number: int):
        return 'P'


'''

def fib()



import math


# 4 mins 
class Solutions1():
    29 / 5
    def check_prim(self, number: int):
        if number < 2:
            return 'NP'

        for i in range(2,int(number**0.5)+1):
            if number % i == 0:
                return 'NP'

        return 'P'


    def axe(self,n: int) -> str:
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                print('Axe')
            elif i % 3 == 0 :
                 print('Paul')
            elif i % 5 == 0:
                 print('Russel')
            else:
                print(f"{self.check_prim(i)}:{i}")
                
        return ''

        
x = Solutions1()
print(x.leomar(15))


