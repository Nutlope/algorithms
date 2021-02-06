class Solution:
    def swap_adjacent_pairs(self, head):
        some_head = head
        list_1 = []
        while (some_head):
            list_1.append(some_head.val)
            some_head = some_head.next
        
        for i in range(0, len(list_1), 2):
            if i + 1 < len(list_1):
                list_1[i], list_1[i + 1] = list_1[i + 1], list_1[i]
        
        new_LL = dummy_head = Node(list_1[0])
        
        for i in range(1, len(list_1)):
            new_LL.next = Node(list_1[i])
            new_LL = new_LL.next
         
        return dummy_head

# Always required that Linked List is O(1)
# OPTIMAL SOLUTION

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