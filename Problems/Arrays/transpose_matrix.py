from typing import List  # Import for static type checking

'''
Leetcode problem 867: Given a matrix A, return the transpose of A. The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
'''

def transpose(A: List[List[int]]) -> List[List[int]]:
    # O(n*m) time | O(n) space, where n*m is the dimension of the matrix

    transpose = []
    # populate transpose matrix with empty arrays
    for i in range(len(A[0])):
        transpose.append([])

    for lst in A:
        for i in range(len(lst)):
            # append each value to appropriate subarray in transpose
            transpose[i].append(lst[i])
    return transpose

# Test Cases
assert transpose([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]]
assert transpose([[1,2,3],[4,5,6],[7,8,9]]) == [[1,4,7],[2,5,8],[3,6,9]]
assert transpose([[1,2,3],[4,5,6],[7,8,9],[11,12,13]]) == [[1,4,7,11],[2,5,8,12],[3,6,9,13]]