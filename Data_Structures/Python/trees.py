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
        return [self.root.val] + self.PreOrder(self.root.left) + self.PreOrder(self.root.right) if self.root else []
    
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