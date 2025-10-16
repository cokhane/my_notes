'''
###how does merge sort work

- so imagine this, 3,23,1,6
- you first need to do divide and conquer
- you split the array into half pieces
- in our example it should be like this

[3,23,1,6]
[3,23] [1,6]
[3] [23] [1] [6]

'''

import math

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    middle_index = len(arr) // 2  
    left_arr = arr[:middle_index]
    right_arr = arr[middle_index:]

    print(f'middle_index: {middle_index}')
    print(f'left_arr: {left_arr}')
    print(f'right_arr: {right_arr}')
    
    return merge(merge_sort(left_arr), merge_sort(right_arr))


def merge(left_arr, right_arr):
    result_arr = []
    left_index = 0
    right_index = 0

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            result_arr.append(left_arr[left_index])
            left_index = left_index + 1
        else:
            result_arr.append(right_arr[right_index])
            right_index = right_index + 1  # fixed

    # add leftovers
    if left_index < len(left_arr):
        result_arr.extend(left_arr[left_index:])
    if right_index < len(right_arr):
        result_arr.extend(right_arr[right_index:])

    return result_arr


print(merge_sort([12,3,16,6,5,1]))

