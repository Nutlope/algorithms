from typing import List  # Import for static type checking

'''
Leetcode problem 547: There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is 
connected directly with city c, then city a is connected indirectly with city c.

NOT A VALID SOLUTION - CHECKS DIAGONALS

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
'''

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows = len(isConnected) # define rows & cols, same size
        # make a parents array
        parent = list(range(rows*rows))
        self.count = 0 # of provinces, set to # of 1s initially
        for i in range(rows):
            for j in range(rows):
                if isConnected[i][j] == 1:
                    self.count += 1
        
        # finds parent
        def find(v):
            while v != parent[v]:
                parent[v] = parent[parent[v]]
                v = parent[v]
            return v
        
        # unionizes by setting 1 parent to the other's
        def union(v1, v2):
            p1 = find(v1)
            p2 = find(v2)
            if p1 == p2: return # don't unionize if part of the same set
            parent[p1] = p2
            self.count -= 1
        
        for i in range(rows):
            for j in range(rows):
                if isConnected[i][j] == 1:
                    index = i*rows + j # to correspond to the parent array indices
                    if j < rows-1 and isConnected[i][j+1] == 1: # check if something to the right
                        union(index, index+1)
                    if i < rows-1 and isConnected[i+1][j] == 1: # check if something is down
                        union(index, index+rows)
                    # check if something is down right
                    if j < rows-1 and i < rows-1 and isConnected[i+1][j+1] == 1:
                        union(index, index+rows+1)
                    # check if something is top right
                    if j < rows-1 and isConnected[i-1][j+1] == 1:
                        union(index, index-rows+1)
        return self.count