/*
Uses: HTML DOM, network routing, Abstract Syntax Trees (ASTs)
Binary Search Trees: Every node to the left is less and node to the right is bigger than it's parent
Time: O(log n) insertion and searching on average & best case (should be balanced). 2nd best after O(1)
Tree Traversal: How do we visit every single node? Breadth First (across, each level) and Depth First (down)
DFS has Preorder, PostOrder, and InOrder 
When do you use BFS vs DFS? Time complexity is the same, look at space complexity
Wider trees, DFS is better, and longer trees BFS is generally better
DFS Inorder gives you a list from smaller to bigger 
*/

class Node {
  constructor(value) {
    this.value = value;
    this.right = null;
    this.left = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }
  insert(val) {
    let newVal = new Node(val);
    if (this.root == null) {
      this.root = newVal;
      return this;
    }
    let curNode = this.root;
    while (true) {
      if (val === curNode.value) return undefined;
      if (newVal.value > curNode.value) {
        if (curNode.right) {
          curNode = curNode.right;
        } else {
          curNode.right = newVal;
          return this;
        }
      } else {
        if (curNode.left) {
          curNode = curNode.left;
        } else {
          curNode.left = newVal;
          return this;
        }
      }
    }
  }
  find(val) {
    if (this.root == null) return false;
    let cur = this.root;
    let found = false;
    while (cur && !found) {
      if (val < cur.value) {
        cur = cur.left;
      } else if (val > cur.value) {
        cur = cur.right;
      } else {
        found = true;
      }
    }
    if (!found) return false;
    return cur;
  }
  //
  BFS() {
    let data = [];
    let queue = [];
    let node = this.root;
    queue.push(node);
    while (queue.length) {
      node = queue.shift();
      data.push(node.value);
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    return data;
  }
  DFSPreOrder() {
    let data = [];
    function traverse(node) {
      data.push(node.value);
      if (node.left) traverse(node.left);
      if (node.right) traverse(node.right);
    }
    traverse(this.root);
    return data;
  }
  DFSPostOrder() {
    let data = [];
    function traverse(node) {
      if (node.left) traverse(node.left);
      if (node.right) traverse(node.right);
      data.push(node.value);
    }
    traverse(this.root);
    return data;
  }
  DFSInOrder() {
    let data = [];
    function traverse(node) {
      if (node.left) traverse(node.left);
      data.push(node.value);
      if (node.right) traverse(node.right);
    }
    traverse(this.root);
    return data;
  }
}

let tree = new BinarySearchTree();
tree.insert(5);
tree.insert(6);
tree.insert(32);
console.log(tree.BFS());
