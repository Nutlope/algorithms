from typing import List  # Import for static type checking

'''
Leetcode problem 200: Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0: 
            return 0
        row = len(grid)
        col = len(grid[0])
        self.count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.count += 1
        parent = list(range(row*col))

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x,y):
            xroot, yroot = find(x),find(y)
            if xroot == yroot: return 
            parent[xroot] = yroot
            self.count -= 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    index = i*col + j
                    if j < col-1 and grid[i][j+1] == '1':
                        union(index, index+1)
                    if i < row-1 and grid[i+1][j] == '1':
                        union(index, index+col)
        return self.count

assert Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]) == 1
assert Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]) == 3