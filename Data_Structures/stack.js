// A LIFO (last in first out) data structure, like pile of dishes
// can implement in a variety of ways

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
