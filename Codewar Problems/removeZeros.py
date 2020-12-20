# Given an array nums, write a function to move all 0's to the end 
# of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# 1. Loop through and remove 0s, count how many removed, then add them at end

def removeZeros(input_list):
    count = 0
    for i in input_list:
        if i == 0:
            input_list.remove(i)
            count += 1
    for i in range(count):
        input_list.append(0)

    return input_list

print(removeZeros([0,1,0,3,12]))