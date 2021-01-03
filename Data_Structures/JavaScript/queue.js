// A FIFO (first in first out) data structure, like waiting in a line or printing docs
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
