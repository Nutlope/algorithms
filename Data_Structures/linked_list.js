// Linked List Implementation
// Linked lists - consists of nodes that are connected to each other, each containing a value and pointer to the next
// 3 things we keep track of: Head is the beginning, tail is the end, and length
// Random access not allowed, have to start searching from the beginning
// If you care about insertion and deletion, you may want to work with linked lists

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }
  // Inserting at the end
  push(val) {
    let new_node = new Node(val);
    if (this.head) {
      this.tail.next = new_node;
      this.tail = new_node;
    } else {
      this.head = new_node;
      this.tail = new_node;
    }
    this.length++;
    return this;
  }
  traverse() {
    let beginning = this.head;
    while (beginning) {
      console.log(beginning.val);
      beginning = beginning.next;
    }
  }
  // Removing at the end
  pop() {
    if (!this.head) {
      return undefined;
    }
    let beginning = this.head;
    while (beginning) {
      if (beginning.next) {
        beginning = beginning.next;
      } else {
        beginning;
      }
    }
  }
}

// let first = new Node("hi");
// first.next = new Node("how");
// first.next.next = new Node("are");
// first.next.next = new Node("you");

let list = new SinglyLinkedList();
console.log(list.push("hello"));
console.log(list.push("goodbye"));
console.log(list.push("cyaa"));
console.log("AAAAAAh");
console.log(list.traverse());
