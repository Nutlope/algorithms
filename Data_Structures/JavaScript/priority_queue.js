// Data structure where each element has a priority. Elements with high priorities are served before elements
// with low priorities. Can be implemented using a binary heap

class Node {
  constructor(val, priority) {
    this.val = val;
    this.priority = priority;
  }
}

// Minimum priority queue (low number priority = high priority)
class PriorityQueue {
  constructor() {
    this.values = [];
  }

  // Inserts node and puts it in right spot (Add to end then bubble up)
  enqueue(val, priority) {
    let element = new Node(val, priority);
    this.values.push(element);
    let idx = this.values.length - 1;
    while (idx > 0) {
      let parentIdx = Math.floor((idx - 1) / 2);
      let parent = this.values[parentIdx];
      if (element.priority >= parent.priority) break;
      this.values[parentIdx] = element;
      this.values[idx] = parent;
      idx = parentIdx;
    }
    return this;
  }
  // Deletes top node and rearranges priority queue
  dequeue() {
    const min = this.values[0];
    const end = this.values.pop();
    this.values[0] = end;
    const length = this.values.length;
    let element = this.values[0];
    let idx = 0;
    while (true) {
      let leftChildIdx = 2 * idx + 1;
      let rightChildIdx = 2 * idx + 2;
      let leftChild, rightChild;
      let swap = null;

      if (leftChildIdx < length) {
        leftChild = this.values[leftChildIdx];
        if (leftChild.priority < element.priority) {
          swap = leftChildIdx;
        }
      }
      if (rightChildIdx < length) {
        rightChild = this.values[rightChildIdx];
        if (
          (rightChild.priority < element.priority && swap === null) ||
          (rightChild.priority < leftChild.priority && swap !== null)
        ) {
          swap = rightChildIdx;
        }
      }
      if (swap === null) break;

      this.values[idx] = this.values[swap];
      this.values[swap] = element;
      idx = swap;
    }
    return min;
  }
}

let some = new PriorityQueue();
some.enqueue("common cold", 5);
some.enqueue("high fever", 4);
some.enqueue("broken shoulder", 3);
some.enqueue("knife in foot", 2);
some.enqueue("gunshot wound", 1);
some.enqueue("knife in head", 1);

console.log(some.dequeue());
console.log(some.values);
