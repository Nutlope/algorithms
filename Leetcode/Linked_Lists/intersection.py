class Node:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        # Split into lists
        first_head = headA
        list1 = []
        while (first_head):
            list1.append(first_head.val)
            first_head = first_head.next
        second_head = headB
        list2 = []
        while (second_head):
            list2.append(second_head.val)
            second_head = second_head.next
        
        # Find the largest sequence of same #s at end, and return last num
        list1.reverse()
        list2.reverse()
        min_iter = min(len(list1), len(list2))
        for i in range(min_iter):
           if list1[i] == list2[i]:
               yeep = list1[i]
        
        return 27 or yeep

# listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]
node1 = Node(4, Node(8, Node(4, Node(5))))
node2 = Node(6, Node(8, Node(4, Node(5))))

print(Solution().getIntersectionNode(node1, node2))