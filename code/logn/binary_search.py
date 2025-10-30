# import math
# def binary_search_not_sorted(n: list, target: int):
#     start = 0
#     end = len(n)-1
    
#     while start <= end:
#         mid = math.floor((start+end)/2)

#         print('mid: ', mid)

#         if n[mid] == target:
#            return mid
        
#         if n[mid] < target:
#            start = mid + 1
           
#         else:
#             end = mid - 1 

#         print('mid value : ',n[mid])
#         print('target : ',target)
#         print('start: ',start)
#         print('end: ',end)

#     return -1 


# print("binary_search: ", binary_search_not_sorted([1,2,7,12,43,44,44,54,100,124],7))

'''
how binary search work?

- it should be sorted
- now lets find the start and end 
- then get mid by star+end/2
- if mid = target return MID - found 
- if mid < target 
    start = mid + 1
else 
    emd = mid - 1

then we go back the top of the loop which is step 3


'''



"""

"""

def binary_search_not_sorted_axe(nlist, target):
    start = 0
    end = len(nlist)-1
    

    i = 0
    while start <= end:
        mid = int((start+end)/2)  

        print(f"mid: {mid}")
        print(f"start: {start}")
        print(f"end: {end}")
        print('--------------:')

        if nlist[mid] == target:
            return mid
        elif nlist[mid] < target:
            start = mid + 1
        elif nlist[mid] > target:
            end = mid - 1

        print('new value:')
        print(f"start: {start}")
        print(f"end: {end}")
    
    return -1 
     






print(f"binary: {binary_search_not_sorted_axe([1,2,7,12,43,44,44,54,100,124],12)}")


































