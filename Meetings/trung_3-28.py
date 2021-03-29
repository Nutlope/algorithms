selection sort & bubble sort
look into heapsort and mergesort
tree problems, dfs (recursively, and iteratively), bfs
binary search

"""
150 x 150 = 22500
0 255
Mat:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
 
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

  [[2,3,4],
   [5,6,7],
   [8,9,10],
[11,12,13],
[14,15,16]]

  [[4,4,5],
   [5,6,6],
   [8,9,9],
[11,12,12],
[13,13,14]]
"""

def smoothenMatrix(mat):
  # create new mat, loop through each element in mat, add all diagonals and surrounding elements, and divide by that number
  # add the number to the new mat
  # return new mat
  total = [0]
  def get_val(i, j):
    total[0] +=  mat[i][j]
    a = cnt = 0
    for dx in (-1, 0, 1):
      for dy in (-1, 0, 1):
        x = i + dx
        y = j + dy
        if  0 <= x < N and 0 <= y < M:
          a += mat[x][y]
          cnt += 1
    return a // cnt
  
  M = len(mat)
  N = len(mat[0])
  sol = [[0] * N for _ in range(M)]
  
  for i in range(len(mat)):
    for j in range(len(mat[0])):
      val = get_val(i, j)
      sol[i][j] = val
  print(total[0])
  return sol
print(smoothenMatrix([[1,1,1], [1,1,1],[1,1,1]]))

"""

[2, 1, 3, 4, 7, 6] k = 1
[2, 3, 1, 4, 7, 6] k = 2
 ^
 min([2, 3, 1])
Sorted -> messed up
upto K away from its original position
arr, K
algo to sort it increasingly

arr = [3, 4, 5, 2, 1, 9, 8, 6, 10, 7], 

i = 0 => [3 4 5 2 1] => 1
i = 1 => [3 4 5 2 9] => 2
i = 2 => 
i = 3 => 
i = 4 => 
i = 5 => 
i = 6 => 
"""
import heapq as heap

# O(NlogK) time
# O(NlogN) merge sort
def sortArray(arr, k):
  L = arr[ : k]
  heap.heapify(L)
  
  for i, val in enumerate(arr):
    if i+k < len(arr):
      heap.heappush(L,arr[i+k])
    arr[i] = heap.heappop(L)
    
  return arr
  


