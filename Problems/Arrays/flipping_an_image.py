from typing import List  # Import for static type checking

'''
Leetcode problem 832: Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
'''

def flipAndInvertImage(A: List[List[int]]) -> List[List[int]]:
    # O(N*2) time | O(1) space
    for lst in A:
        lst.reverse()
        for i in range(len(lst)):
            # bitwise XOR to invert (0->1 & 1-> 0)
            lst[i] = lst[i]^1
    return A

# Test Cases
assert flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]) == [[1,0,0],[0,1,0],[1,1,1]]
assert flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]) == [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]