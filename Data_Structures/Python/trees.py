'''
Two variations: Binary Trees and Binary search trees.
Main things: BFS & DFS.

Uses: HTML DOM, network routing, Abstract Syntax Trees (ASTs)
Binary Search Trees: Every node to the left is less and node to the right is bigger than it's parent

Ex:   4
    2   7
   1 3  5 11


Time: O(log n) insertion and searching on average & best case (should be balanced). 2nd best after O(1)
Tree Traversal: How do we visit every single node? Breadth First (across, each level) and Depth First (down)
DFS has Preorder, PostOrder, and InOrder 
When do you use BFS vs DFS? Time complexity is the same, look at space complexity
Wider trees, DFS is better, and longer trees BFS is generally better
DFS Inorder gives you a list from smaller to bigger 
'''

# Binary Search Trees - BFS and DFS
import collections

class Node:
    def __init__(self, val):
        self.value = val
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def BFS(self):
        root = self.root
        if root is None:
            return []

        data = []
        queue = collections.deque([root])
        while queue:
            root = queue.popleft()
            data.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return root

    def PreOrder(self, root):
        if not self.root:
            return []
        return [self.root.val] + self.PreOrder(self.root.left) + self.PreOrder(self.root.right)
    
    def PostOrder(self, root):
        return self.PostOrder(self.root.left) + self.PostOrder(self.root.right) + [self.root.val] if self.root else []
    
    def InOrder(self):
        data = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            data.append(node.val)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return data