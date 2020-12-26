class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first_head = l1
        list1 = []
        while (first_head):
            list1.append(first_head.val)
            first_head = first_head.next
        
        second_head = l2
        list2 = []
        while (second_head):
            list2.append(second_head.val)
            second_head = second_head.next
        
        # go from list to number and add
        num1 = int(''.join(map(str,list1)))
        num2 = int(''.join(map(str,list2)))
        final_num = num1 + num2
        
        # make list from numbers
        final_list = list(str(final_num)) # str of nums

        # make LL from numbers
        final_head = dummy = ListNode(final_list[0])
        
        for i in range(1,len(final_list)):
            final_head.next = ListNode(final_list[i])
            final_head = final_head.next
        
        return dummy 