import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
        
root1 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(5)), TreeNode(6, None, TreeNode(7, None, TreeNode(8)))) # pre
root2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6, None, TreeNode(7, None, TreeNode(8)))) # in
root3 = TreeNode(8, TreeNode(4, TreeNode(2, TreeNode(1)), TreeNode(3)), TreeNode(7, None, TreeNode(6, None, TreeNode(5)))) # post
root4 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)), TreeNode(3, None, TreeNode(6, None, TreeNode(8))))

# list BFS, DFS Graph problem, preorder, postorder, inorder only for tree
1, 1, 2, 3, 5, 8
def dfs(n): 4
    base 2, 1
    dfs(n - 1) + dfs(n - 2)

# BFS DFS
# Space: O(2^N)
# Time 

def BFS(root):
    if root is None:
        return []
    
    queue = [root]
    data = []
    while queue:
        cur = queue.pop(0)
        data.append(cur.val)     
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return data

def PreOrder(root):
    return [node.val] + PreOrder(node.left) + PreOrder(node.right) if node else []

def InOrder(root):
    data = []
    def traverse(node):
        if node:
            if node.left:
                traverse(node.left)
            data.append(node.val)        
            if node.right:
                traverse(node.right)
    traverse(root)
    return data
    
# var = 5
def PostOrder(root):
    data = []
    def traverse(node):
        if node:
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            data.append(node.val)
    traverse(root)
    return data


# print(PreOrder(root1))
# print(InOrder(root2))
# print(PostOrder(root3))
# queue = [[depth, NODE], [0, NODE], [0, NODE]]
# O(N) space, O(N) time
def deepestLeafs(root):
    if root == None: return 0
    deepest = 1
    queue = collections.deque([[0, root]])
    # getting deepest
    while queue:
        depth, cur = queue.popleft()
        deepest = max(deepest, depth)
        if cur.left: queue.append([depth + 1, cur.left])
        if cur.right: queue.append([depth + 1, cur.right])
    
    total = 0
    queue = collections.deque([[0, root]])
    while queue:
        depth, cur = queue.popleft()
        if cur.left == cur.right == None and depth == deepest: # gets all the leaves and sums them
            total += cur.val
        if cur.left:
            queue.append([depth + 1, cur.left])
        if cur.right:
            queue.append([depth + 1, cur.right])
    return total

def deepestLeafs(root):
    if root == None: return 0
    queue = collections.deque([[0, root]])
    nodes = []
    while queue:
        depth, cur = queue.popleft()
        if depth >= len(nodes):
            nodes.append([])
        nodes[depth].append(cur.val)
        if cur.left: queue.append([depth + 1, cur.left])
        if cur.right: queue.append([depth + 1, cur.right])
    return sum(nodes[-1])

def deepestLeafs(root):
    if root == None: return 0
    queue = collections.deque([[0, root]])
    total = deepest = 0
    while queue:
        depth, cur = queue.popleft()
        if depth > deepest:
            deepest = depth
            total = 0
        total += cur.val
        if cur.left: queue.append([depth + 1, cur.left])
        if cur.right: queue.append([depth + 1, cur.right])
    return total

print(deepestLeafs(root4))
