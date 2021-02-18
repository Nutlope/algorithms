'''
A set of nodes and connections
Uses: Routing algorithms, Location/Mapping, Social Networks, recommendation engines

Terminology: Vertex = node and edge = connections
Undirected graph: No direction associated with a vertex, can be back and forth
Directed graph: There's a direction associated with a vertex
Weighted graph: Each edge has a weight

Can implement with an adjacency list or adjacency matrix. 

- Adjacency list is faster and uses less space for sparse graphs (edges and vertices about equal), but is slower for dense graphs.
- Adjacency matrices are faster for dense graphs, easier to implement weighted graph, but they use more space (V^2)
'''

# implement undirected graph with adjacency list
class Graph:
  def __init__(self):
    self.adjacencyList = {}
  def __str__(self):
    return str(self.adjacencyList)

  def addVertex(self, vertex):
    if vertex not in self.adjacencyList:
      self.adjacencyList[vertex] = []
  
  def addEdge(self, v1, v2):
    if v1 not in self.adjacencyList or v2 not in self.adjacencyList:
      raise Exception("Create the vertices you want to connect first. ")
    self.adjacencyList[v1].append(v2)
    self.adjacencyList[v2].append(v1)
  
  def removeEdge(self, v1, v2):
    self.adjacencyList[v1].remove(v2)
    self.adjacencyList[v2].remove(v1)

  def removeVertex(self, vertex):
    # delete the actual list of the vertext
    del self.adjacencyList[vertex]
    # delete it from all other adjacency lists
    for obj in self.adjacencyList:
      if vertex in self.adjacencyList[obj]:
        self.adjacencyList[obj].remove(vertex)
  
  def BFS(self):
    # start at arbitrary vertex & add to a queue
    # explore elemements one by one from the queue, add all their neighbors to it.
      # take element out of queue when explored all of it's neighbors
    # keep going until there are no more elements in the queue
    pass

  def DFS_R(self):
    # start at arbitrary vertex & add to a stack
    # explore elements one by one from the stack, going deeper and deeper
    pass

graph = Graph()
graph.addVertex(5)
graph.addVertex(6)
graph.addVertex(7)
graph.addEdge(5,6)
graph.addEdge(5,7)
graph.removeEdge(5,7)
graph.removeVertex(7)
print(graph)

# BFS - Start from a vertex, visit all neighbors, then go to next vertex, visit all neighbors. Level by level.

# DFS - Start from a vertex, visit 1 neighbor, visit its neighbor, & keep going until it's completely explored.
# Then work your way back exploring all neighbors

'''
Resources:
https://www.youtube.com/watch?v=j0IYCyBdzfA&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=12&ab_channel=codebasics
https://www.youtube.com/watch?v=pcKY4hjDrxk&ab_channel=AbdulBari
https://www.geeksforgeeks.org/union-find/
https://algocoding.wordpress.com/2014/09/19/union-find-data-structure-disjoint-set-data-structure/
https://algocoding.wordpress.com/2014/09/25/union-find-data-structure-disjoint-set-data-structure-part-2/
'''

# WTDs rn
# 1. Go over BFS and DFS implementations in Python
# 2. Play around with union find within graphs myself
# 3. Revisit leetcode problems

# General WTD: Go over python data structures and algos repo