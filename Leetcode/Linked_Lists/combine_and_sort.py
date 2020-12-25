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

node1 = Node(1, Node(2, Node(4, Node(7))))
node2 = Node(3, Node(8, Node(9)))

class Solution:
  def sortedList(self, head1, head2):
    # # combine linked lists
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
    
    L = [1,2,3]
    L.append(L)
    print(L)
    print(L[3])
    
    # b = 6   
    # head = new_LL = ...
    # sorted_arr = []
    # while node1 or node2:
    #   if node1 and node2:
    #     if node1.val < node2.val:
    #       prev.next = node1
    #       prev = prev.next
    #       node1 = node1.next
    #     else:
    #       prev.next = node2
    #       prev = prev.next
    #       node2 = node2.next
    #   else:
    #     node = node1 or node2
    #     while node:
    #       Node(node.val)
    #       node = node.next
    #     break
    
    
    
print(Solution().sortedList(node1, node2))

# always append and add from end

# OLD Solution

# class Node:
#   def __init__(self, val, nxt=None):
#     self.val = val
#     self.next = nxt
#   def __str__(self):# d-under methods
#     rv = []
#     node = self
#     while node:
#       rv.append(node.val)
#       node = node.next
#     return str(rv)

# """
# 1->2->4->7
# 3->8->9

# 1->2->3->4->7->8->9
# """

# node1 = Node(1, Node(2, Node(4, Node(7))))
# node2 = Node(3, Node(8, Node(9)))

# class Solution:
#   def sortedList(self, head1, head2):
#     # combine linked lists
#     first_start = something = head1
#     # list of first linked list
#     first_L = []
#     while something:
#       first_L.append(something.val)
#       something = something.next
#     second_start = second = head2
#     # list of second linked list
#     second_L = []
#     while second:
#       second_L.append(second.val)
#       second = second.next
      
#     while first_start:
#       first_start = first_start.next
#       if not first_start.next:
#         first_start.next = head2
#         break

#     first_L.reverse()
#     second_L.reverse()
#     # sort them. We have first_L and second_L
#     sorted_arr = []
#     while first_L or second_L:
#       if first_L and second_L:
#         if first_L[-1] < second_L[-1]:
#           val = first_L.pop()
#           sorted_arr.append(val)
#         else:
#           val = second_L.pop()
#           sorted_arr.append(val)
#       elif first_L:
#         val = first_L.pop()
#         sorted_arr.append(val)
#       elif second_L:
#         val = second_L.pop()
#         sorted_arr.append(val)
        
#     head = new_LL = Node(sorted_arr[0])
#     for i in range(1,len(sorted_arr)):
#       new_LL.next = Node(sorted_arr[i])
#       new_LL = new_LL.next
    
#     return head
    
# print(Solution().sortedList(node1, node2))