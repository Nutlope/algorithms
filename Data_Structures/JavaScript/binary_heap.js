/* 
A tree structure, where the parent is always bigger than the children for a max binary heap
Two values max under each node. Left children are filled up first. Evenly distributed
Binary Heaps are mostly used for priority queues
Can implement binary heap with array. children are at 2n + 1 for L and 2n + 2 where n is index of parent
2 variations: Max Binary Heap or Min Binary Heap
BIG O: O(log N) insertion and removal, O(N) search
 */

class MaxBinaryHeap {
  constructor() {
    this.values = [41, 39, 33, 18, 27, 12];
  }
  // 1. Add to end (start at end node on left)
  // 2. bubble up (compare with above, if bigger, swap and keep going)
  insert(element) {
    this.values.push(element);
    this.bubbleUp(element);
    return this;
  }
  bubbleUp(element) {
    let idx = this.values.length - 1;
    while (idx > 0) {
      let parentIdx = Math.floor((idx - 1) / 2);
      let parent = this.values[parentIdx];
      if (element <= parent) break;
      this.values[parentIdx] = element;
      this.values[idx] = parent;
      idx = parentIdx;
    }
  }
  // remove the top most element and restructure binary heap
  extractMax() {
    const max = this.values[0];
    const end = this.values.pop();
    this.values[0] = end;
    this.sinkDown();
    return max;
  }
  sinkDown() {
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
        if (leftChild > element) {
          swap = leftChildIdx;
        }
      }
      if (rightChildIdx < length) {
        rightChild = this.values[rightChildIdx];
        if ((rightChild > element && swap === null) || (rightChild > leftChild && swap !== null)) {
          swap = rightChildIdx;
        }
      }
      if (swap === null) break;

      this.values[idx] = this.values[swap];
      this.values[swap] = element;
      idx = swap;
    }
  }
}

let heap = new MaxBinaryHeap();
console.log(heap.insert(55));
console.log(heap.extractMax());
console.log(heap.values);
