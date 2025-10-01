import math 

list = [1,2,3,4,5,6,7,8]
start = 0
end = len(list) - 1
target = 5

def binarySearch(list,start,end,target):
    midIndex = math.floor((start+end)/2)
    if list[midIndex] == target:
        return midIndex
    
    if list[midIndex] > target:
        return binarySearch(list,start,midIndex-1,target)
    else:    
        return binarySearch(list,midIndex+1,end,target)
    

print('index: ',binarySearch(list,start,end,target))