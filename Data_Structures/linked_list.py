# Linked List Implementation

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

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

list = SinglyLinkedList()
list.push("hello")
list.push("goodbye")
list.push("cyaa")

# Is there an easy way in python to print out this whole thing?
print(list.head.val)
print(list.tail.val)
print(list.length)