
# head -> 1 - 2 - 3 - 4
# head -> 2 - 1 - 4 - 3

class Node:
  def __init__(self, val, nxt=None):
    self.val = val
    self.next = nxt
    
  def __str__(self):
    rv = []
    node = self
    while node:
      rv.append(node.val)
      node = node.next
    return str(rv)

# Space: O(1)
# Space optimization
# Time:
# timsort()

head1, head2 -> combined head


# [head1, head2, ... headk] -> combined head
# array -> sorted -> return O(NlogN) N is total nodes
# heap, Priority Queue,  O(NlogK)

class Solution:
    def dfs(self, node): # O(N). All recursion solutions can be written iteratively.
        if not node or not node.next: return 
        first = node; second = first.next; third = second.next
        second.next = first
        first.next = self.dfs(third)
        return second
    
    def f1(self, node):
        stack = []
        while node and node.next:
            first = node; second = first.next; third = second.next
            second.next = first
            stack.append([second, first])
            node = third
        print(list([row[0].val, row[1].val] for row in stack))
    
    def swap_adjacent_pairs(self, head):
        cur = head = Node(None, head)        
        while cur.next and cur.next.next:  
            # None, 1, 2, 3
            # 2, 3, 4, None => 2 -> 4 -> 3 -> None
            # None, None, None, None
            
            first = cur.next # Node(1, Node(2, None))
            second = first.next # Node(2, None)
            third = second.next # None
            
            second.next = first
            first.next = third
            cur.next = second
            
            cur = cur.next.next
        return head.next
node = Node(1, Node(2))
node = Node(1, Node(2, Node(3, Node(4))))
print(Solution().swap_adjacent_pairs(node))

node2 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(Solution().f1(node2))