from typing import List  # Import for static type checking

'''
Leetcode problem 66: Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit. You may assume the integer does not contain any leading zero, except the number 0 itself.
'''

def plusOne(digits: List[int]) -> List[int]:
    # O(N) time | O(1) space
    if len(digits) == 1 and digits[0] == 9:
        return [1, 0]
    
    # if last digit isn't 9, add one to end and return
    if digits[-1] != 9:
        digits[-1] += 1
        return digits
    # if it is 9, set to 0 and run solution recursively without last digit
    else:
        digits[-1] = 0
        digits[:-1] = plusOne(digits[:-1])
        return digits  

# Test Cases
assert plusOne([4,3,2,1]) == [4,3,2,2]
assert plusOne([1,9,9,9]) == [2,0,0,0]
assert plusOne([1,2,3]) == [1,2,4]
assert plusOne([0,0]) == [0,1]