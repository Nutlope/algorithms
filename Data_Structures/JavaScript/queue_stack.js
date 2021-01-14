// Queue: A FIFO (first in first out) data structure, like waiting in a line or printing docs
// BIG O: Insertion and removal is O(1)
// BIG O: Searching and access is O(N)

// Array implementation: add to end and remove from beginning
let queue = [];
queue.push("first"); // adds to end
queue.push("second");
queue.push("third");
queue.shift(); // removes from beginning

// Array implementation v2: unshift combined with pop - Not ideal due to O(1)
queue.unshift("first");
queue.unshift("second");
queue.unshift("third");
queue.pop();

// Stack: A LIFO (last in first out) data structure, like pile of dishes or CTRL-Z to undo/redo
// BIG O: Insertion and removal is O(1), isn't that same as Linked List??
// BIG O: Searching and access is O(N)

// Array implementation - add and remove from end
let stack = [];
stack.push(1);
stack.push(2);
stack.pop();

// Array implementation #2 - add and remove from beginning
stack.unshift(1);
stack.unshift(2);
stack.shift();

// Linked List implementation with push and pop (except add/remove from beginning b/c we want it to be O(1))
