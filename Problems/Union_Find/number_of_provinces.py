from typing import List  # Import for static type checking

'''
Leetcode problem 547: There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows = len(isConnected) # define rows & cols, same size
        parent = list(range(rows)) # make a parents array
        self.count = rows # of provinces, set to # of cities initially
        
        def find(v):
            # finds parent
            while v != parent[v]:
                parent[v] = parent[parent[v]]
                v = parent[v]
            return v
        
        def union(v1, v2):
            # unionizes by setting 1 parent as the other's parent
            p1, p2 = find(v1), find(v2)
            if p1 == p2: return # don't unionize if part of the same set
            parent[p1] = p2
            self.count -= 1
        
        for i in range(rows):
            for j in range(rows):
                # check if row is connected to another. if it is, unionize them
                if isConnected[i][j] == 1:
                    union(i,j)
        return self.count

assert Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]) == 1
assert Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2
assert Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3
