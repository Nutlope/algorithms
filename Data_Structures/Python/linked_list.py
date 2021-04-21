'''
Linked List Implementation
Linked lists - consists of nodes that are connected to each other, each containing a value and pointer to the next
3 things we keep track of: Head is the beginning, tail is the end, and length
If you care about insertion and deletion, it's O(1) with LL. This is either O(1) or O(N) with arrays depending on if inserting in the front or back.
If you care about accessing and searching, arrays are probably better since they're O(1) but O(N) with LL
'''
# Linked List Implementation

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __str__(self):
        rv = []
        node = self
        while node:
            rv.append(node.val)
            node = node.next
        return str(rv)

class SinglyLinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def print(self):
        rv = []
        node = self.head
        while node:
            rv.append(node.val)
            node = node.next
        print(rv)

    # Inserting at the end
    def push(self, val):
        new_node = Node(val)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return self

    # Remove at the end
    def pop(self):
        if self.head is None: 
            return None
        cur = self.head
        while cur.next.next:
            cur = cur.next
        self.tail = cur
        cur.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        return cur

    # Remove from the beginning
    def shift(self):
        if self.head is None: 
            return None
        cur = self.head
        new_head = cur.next
        self.head = new_head
        cur.next = None
        self.length -= 1
        if (self.length == 0):
            self.tail = None
        return self
    
    # Adding from the beginning
    def unshift(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            cur = self.head
            self.head = new_node
            new_node.next = cur
        self.length += 1
        return self
    
    # Get value of a node at index
    def get(self, idx):
        cur = self.head
        counter = 0
        while cur:
            if counter == idx:
                return cur
            cur = cur.next
            counter +=1
    
    # Set value of a node at index
    def set(self, val, idx):
        found_node = self.get(idx)
        if found_node:
            found_node.val = val
            return True
        return False

    # Insert node at an index
    def insert(self, val, idx):
        if idx < 0 or idx >= self.length:
            return False
        
        if idx == 0:
            return self.unshift(val) # figure out how to return boolean
        
        new_node = Node(val)
        cur = self.get(idx)
        if cur == self.tail:
            return self.push(val)
        old_next = cur.next
        cur.next = new_node
        new_node.next = old_next
        self.length += 1
        return True
    
    # Remove node at an index
    def remove(self, idx):
        if idx < 0 or idx >= self.length:
            return False
        
        if idx == 0:
            return self.shift() # figure out how to return boolean
        
        cur = self.get(idx)
        if cur == self.tail:
            return self.pop()
        prev = self.get(idx-1)
        removed = prev.next
        prev.next = cur.next
        self.length -= 1
        return removed

    # Reverse in-place in O(1) space
    def reverse(self):
        node = self.head
        self.head = self.tail
        self.tail = node
        prev = None
        
        for i in range(self.length):
            next = node.next
            node.next = prev
            prev = node
            node = next


list = SinglyLinkedList()
list.push("hello")
list.push("goodbye")
list.push("cyaa")
list.reverse()
list.print()