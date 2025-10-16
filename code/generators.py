# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result

#generator
def square_numbers(nums):
    for i in nums:
        yield (i*i)


my_nums = square_numbers([1,2,3,4,5])

for num in my_nums:
    print(num)
    
'''
generators dont hold the entire result in memory, it yields one result at a time
'''