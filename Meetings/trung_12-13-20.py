# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

#  O(N) O(1)

# [-2,1,-3,4,-1,2,1,-5,4]
# => 6 
# -1
# O(N^3). O(1)
def return_largest(nums):
  # loop through arr, store value of 2, 3, ... len(nums) continuous elements with the greatest sum
  largest = -9999
  # This returns largest sum of 1, 2, 3,4  continuous values
  for start in range(len(nums)):
    for end in range(start, len(nums)):
      total = sum(nums[start:end + 1]) #O(N)
      if total > largest:
        largest = total
  return largest

print(return_largest([-2,1,-3,4,-1,2,1,-5,4]))
print(return_largest([-2,-1,-3, -5, -7]))

# prefix_sum == cummulative sum
# [-2, 1,-3,4,-1,2,1,-5,4]
# [0 -2 -1 -4 0 -1 1 2 -1 2] O(N)

# [-2, 1,-3,4,-1,2,1] = 2
# [-2, 1,-3] = -4
# 2 - (-4) =6
"""
prefix_sum = [...] O(N)
for start:
  for end:
    total = prefix_sum[end] - prefix_sum[start]
"""

# Dynamic programming
# O(N^2). O(N). Brute force
def return_largest_2(nums):
  prefix_sum = [0]
  for num in nums:
    prefix_sum.append(num + prefix_sum[-1])
  
  largest = -9999
  [1,2,....]
  # create_list -> get_max O(N)
  # generators -> get_value -> get_max -> get_value -> get_max, less memory. O(1) space
  return max(end - start for i, start in enumerate(nums) for end in nums[i + 1:])
  
  # for start in range(len(nums)):
  #   for end in range(start + 1, len(nums)):    
  #     total = prefix_sum[end] - prefix_sum[start]
  #     largest = max(largest, total)
  # return largest

print("-------O(N)------")
print(return_largest([-2,1,-3,4,-1,2,1,-5,4]))  
print(return_largest_2([-2,-1,-3, -5, -7]))

# O(N). O(N)
def return_largest_3(nums):
  prefix_sum = [...]
  min_sofar = [...]
  for end in ... :
    total = prefix_sum[end] - min_sofar[end] # O(1)
    
  # [0 -2 -1 -4 0 -1 1 2 -1 2] O(N)
  #                         ^
  #                         |
  #                         end
  
  # [0 -2 -2 -4 -4 -4 -4 -4 -4]
                            |
                            end
  
  # [-2 -3 -6 -11 -18]
  #                |
  #               end
  # => -7
  nums => prefix_sum -> min_sofar
  
# O(N) O(1)