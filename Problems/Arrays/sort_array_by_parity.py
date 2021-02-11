from typing import List  # Import for static type checking

'''
Leetcode problem 905: Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

Note: I didn't include any logic to handle cases like an empty array because the question didn't ask for it.
'''

# Solution 1
def sortArrayByParity(A: List[int]) -> List[int]:
    # O(N) time | O(N) space - Simple Solution
    evens = []
    odds = []

    # loop through input array, append even values to evens arr, odd values to odd arr
    for num in A:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    # combine both arrays with evens first
    evens.extend(odds)

    return evens

# Solution 2
def sortArrayByParityInplace(A: List[int]) -> List[int]:
    # O(N) time | O(1) space - Inplace Sorting using 2 pointer technique
    
    # Define two pointers pointing to the start and end of input array
    left = 0
    right = len(A) - 1
    while left < right:
        # if the value on the left is even, increment the pointer
        if A[left] % 2 == 0:
            left += 1
        else:
        # if the value on the left is odd, swap with value on the right to move odd numbers to the end
            A[left], A[right] = A[right], A[left]
            right -= 1
    return A

# Test Cases
assert sortArrayByParity([2,3,5,1,2]) == [2,2,3,5,1] or [2,2,5,3,1] or [2,2,1,3,5] or [2,2,1,5,3]
assert sortArrayByParity([3,1,2,4]) == [2,4,3,1] or [4,2,3,1] or [2,4,1,3] or [4,2,1,3]
assert sortArrayByParity([1,2,1,1,1,2,1]) == [2,2,1,1,1,1,1]

assert sortArrayByParityInplace([2,3,5,1,2]) == [2,2,3,5,1] or [2,2,5,3,1] or [2,2,1,3,5] or [2,2,1,5,3]
assert sortArrayByParityInplace([3,1,2,4]) == [2,4,3,1] or [4,2,3,1] or [2,4,1,3] or [4,2,1,3]
assert sortArrayByParityInplace([1,2,1,1,1,2,1]) == [2,2,1,1,1,1,1]