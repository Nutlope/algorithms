'''
Union Find / Disjoint sets are a data structure that keep track of elements splint into 1 or more disjoint sets
It has 2 primary operations: Find and Union.
Find: Locates which set an element falls under by comparing parents
    keep going through until the parent equals the vertex itself to find parent.
Union: Checks the two nodes, if they belong to 2 diff sets, make one of the parents the other's parent
- If you take any edge in a graph and both vertices belong to the same set, there is a cycle in the graph
'''

s1 = [1,2,3,4]
s2 = [5,6,7,8]
s3 = [1,2,3,4,5,6,7,8] # Union (4,8) -> Union s1 and s2

# Taking a graph, break it down into sets based on the edges, then perform union on sets where edges correspond to diff sets

# How to represent sets in an array?
# [1, 2, 3, 4, 5] (parents of verticies, initially vertices themselves)
#  1  2  3  4  5  (index of arr representing the vertices)
#  A  F  G  H  R (vertices)

# Kruskal's Minimum Spanning tree algorithm

# 1. Sort all edges by weight from least to greatest
# 2. Go weight by weight and perform unions to create different sets and join some
# 3. Any edges that would lead to a cycle, we should skip

class Union:
    def __init__(self):
        self.id = {} # Keeps track of vertices & parents {vertex: parent}
        self.sz = {} # Keeps track of how big each set is {vertex: size}
        self.count = 0 # keeps track of total count of sets
    def __str__(self):
        return "id: " + str(self.id) + '\n' + "size: " + str(self.sz) + '\n' + "count: " + str(self.count)
    def add(self, p):
        # adds a vertex and assigns it to be its own parent
        self.id[p] = p
        self.sz[p] = 1
        self.count += 1

    def find(self, i):
        # returns parent of a vertex
        id = self.id
        while i != id[i]:
            id[i] = id[id[i]]
            i = id[i]
        return i

    def union(self, p, q):
        # unionizes two sets
        i, j = self.find(p), self.find(q)
        if i == j:
            # if both vertices are in the same set, don't unionize
            return
        if self.sz[i] > self.sz[j]:
            i, j = j, i
        # assign one parent to be the parent of the other
        self.id[i] = j
        self.sz[j] += self.sz[i] # increases size of set
        self.count -= 1 # decrease count of sets

union = Union()
union.add(1)
union.add(2)
union.add(3)
union.add(4)
union.add(5)
union.union(4,5)
print(union)