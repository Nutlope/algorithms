// Linked List Implementation
// Linked lists - consists of nodes that are connected to each other, each containing a value and pointer to the next
// 3 things we keep track of: Head is the beginning, tail is the end, and length
// If you care about insertion and deletion (esp from beginning), it's O(1) with LL
// If you care about accessing and searching, arrays are probably better since they're O(1) but O(N) with LL
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
  // 1 -> 2 -> 3 -> 4 Point last node to null & move tail to before last
  pop() {
    if (!this.head) {
      return undefined;
    }
    let cur = this.head;
    let new_tail = this.head;
    while (cur.next) {
      new_tail = cur;
      cur = cur.next;
    }
    this.tail = new_tail;
    new_tail.next = null;
    this.length--;
    // Check if there's nothing in the list to reassign head and tail
    if (this.length == 0) {
      this.head = null;
      this.tail = null;
    }
    return cur;
  }

  // removing from the beginning
  shift() {
    if (!this.head) return undefined;
    let cur = this.head;
    let new_head = cur.next;
    this.head = new_head;

    cur.next = null;
    this.length--;
    if (this.length == 0) {
      this.tail = null;
    }
    return this;
  }

  // adding node to the beginning
  unshift(val) {
    let new_node = new Node(val);
    if (!this.head) {
      this.head = new_node;
      this.tail = new_node;
    } else {
      let cur = this.head;
      this.head = new_node;
      new_node.next = cur;
    }
    this.length++;
    return this;
  }
  // get the value of a node at an index
  get(idx) {
    let cur = this.head;
    let counter = 0;
    while (cur) {
      if (counter == idx) {
        return cur;
      }
      cur = cur.next;
      counter++;
    }
  }
  // set the value of a node at an index
  set(val, idx) {
    let found_node = this.get(idx);
    if (found_node) {
      found_node.val = val;
      return true;
    }
    return false;
  }
  // insert a node at an index
  insert(val, idx) {
    // return false if index isn't within range
    if (idx < 0 || idx >= this.length) return false;

    // insert at beginning if index is 0
    if (idx == 0) return !!this.unshift(val);

    // insert right after the idx if it's b/w 1-len(list) & insert between if other
    let new_node = new Node(val);
    let cur = this.get(idx);
    if (cur == this.tail) return !!this.push(val);

    let old_next = cur.next;
    cur.next = new_node;
    new_node.next = old_next;
    this.length++;
    return true;
  }
  // remove a node at an index
  remove(idx) {
    // return false if index isn't within range
    if (idx < 0 || idx >= this.length) return false;

    // remove at beginning if index is 0
    if (idx == 0) return !!this.shift();

    let cur = this.get(idx);
    if (cur == this.tail) return !!this.pop();
    let prev = this.get(idx - 1);
    let removed = prev.next;
    prev.next = cur.next;
    this.length--;
    return removed;
  }
  reverse() {
    // Reverse Linked List in place in O(1) space
    let node = this.head;
    this.head = this.tail;
    this.tail = node;
    let prev = null;
    let next;

    for (let i = 0; i < this.length; i++) {
      next = node.next;
      node.next = prev;

      prev = node;
      node = next;
    }

    // set last value to this.head

    // Reverse Linked List through making a list
    // let curHead = this.head;
    // let listLL = [];
    // while (curHead) {
    //   listLL.push(curHead.val);
    //   curHead = curHead.next;
    // }
    // listLL.reverse();
    // let new_LL = new Node(listLL[0]);
    // this.head = new_LL;
    // for (let i = 1; i < listLL.length; i++) {
    //   new_LL.next = new Node(listLL[i]);
    //   new_LL = new_LL.next;
    // }
    // return true;
  }
}

let list = new SinglyLinkedList(); // defining linked list

list.push("1");
list.push("2");
list.push("3");
// console.log(list.insert("999", 1));
// list.remove(1);
list.reverse();
list.traverse();
