class Node:
  def __init__(self, val, nxt=None):
    self.val = val
    self.next = nxt
  def __str__(self):# d-under methods
    rv = []
    node = self
    while node:
      rv.append(node.val)
      node = node.next
    return str(rv)

"""
1->2->4->7
3->8->9

1->2->3->4->7->8->9
"""

Valid Number
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
"e2e10" => false
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

# engine=re.compile(r"^[+-]?((\d+\.?\d*)|(\d*\.?\d+))(e[-+]?\d+)?$")
regex
node1 = Node(1, Node(2, Node(4, Node(7))))
node2 = Node(3, Node(8, Node(9)))

Tree < Str ~ Array

Tree vs Graph
DP 

[1,2,3,4,5,6]
[1,3,6,10,15,21]

class Solution:
  def sortedList(self, head1, head2):
    # combine linked lists
    # first_start = something = head1
    # # list of first linked list
    # first_L = []
    
    # while something:
    #   first_L.append(something.val)
    #   something = something.next
    # second_start = second = head2
    
    # # list of second linked list
    # second_L = []
    # while second:
    #   second_L.append(second.val)
    #   second = second.next
      
    # while first_start:
    #   first_start = first_start.next
    #   if not first_start.next:
    #     first_start.next = head2
    #     break
 
    # first_L.reverse()
    # second_L.reverse()
    # # sort them. We have first_L and second_L
    # sorted_arr = []
    # while first_L or second_L:
    #   if first_L and second_L:
    #     if first_L[-1] < second_L[-1]:
    #       sorted_arr.append(first_L.pop())
    #     else:
    #       sorted_arr.append(second_L.pop())
    #   else:
    #     sorted_arr.extend(first_L or second_L)
    #     break
    #   prev = 2.next -> 3
    # node1 = head1; node2 = head2
    # head = prev = Node(None)
    
    # head = Node(None)
    # prev = head
    
    import collections
    D = collections.deque()
    D.append()
    D.pop()
    D.appendleft()
    D.popleft()
    
    D[7] # O(N)
    D[4] # O(1)
    
    L.append(val)
    L = [1,2,3]
    L.append(L)
    print(L)
    print(L[3])
    
print(Solution().sortedList(node1, node2))