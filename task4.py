'''
Analyze why:
     def solution(nums):
         for i in nums:
             if 0 in nums:
                 nums.remove(0)
                 nums.append(0)
         return nums
isn t the best solution.

1. Kompleksnost koda:
    for petlja o(n)
    .remove() o(n)
    --> pa je kompleksnost o(n^2)

2. Izmena liste kroz koju iteriramo?
'''

nums = [1,0,0,1,2,3,0,5,6,0,11,0,23,44,10,0,2,0,3,4]
new_list = [num for num in nums if num != 0]

len_difference = len(nums) - len(new_list)

for i in range(len_difference):
    new_list.append(0)

print(new_list)