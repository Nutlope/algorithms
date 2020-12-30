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
        cur = new_tail = self.head
        while cur.next:
            new_tail = cur
            cur = cur.next
        self.tail = new_tail
        new_tail.next = None
        self.length += 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return cur

list = SinglyLinkedList()
list.push("hello")
list.push("goodbye")
list.push("cyaa")
list.pop()
list.print()