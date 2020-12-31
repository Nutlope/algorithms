// A LIFO (last in first out) data structure, like pile of dishes or CTRL-Z to undo/redo
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
