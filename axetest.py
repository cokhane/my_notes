





"""



kung ang i  divisible ng 3 at 5 didisplay mo axe
pag ang i divisible ng 3 , russel
pag ang i divisible ng 5, paul
if wala sa tatlo yung choice
yung number i determine kung prime or not prime


sample output:

n = 15 

1:NP ,2:P ,paul ,4:P ,russel,paul,7:P,8:P,paul,russel,11:P,paul,13:P,14:P,axe

sample prime number:

2, 3 , 5, 7, 11, 13

what is prime?
a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 


#use this boiler plate:

class Solution():
    def leomar(self,n):
        return 'test'


"""





class Solution():
    

    def leomar(self,n):
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                print("axe")
            elif i % 5 == 0: 
                print("russel")
            
            elif i % 3 == 0:
                print("paul")
            else:
                print(f"{i}:{self.prime(i)}")

        return ''

    def prime(self,n):
        if n < 2:
            return "NP"
        
        for i in range(2,int(n** 0.5) + 1):
            if n % i  == 0:
                return 'NP'
            
        return 'P'





axe = Solution()
print(f"{axe.leomar(15)}")