/* Hash tables are key-value pairs that aren't indexed. They are dictionaries in Python
We need a way to convert a key to an index (hash function)
hash function: map input to an output of a fixed size
What makes a good hash function? 
    - fast (O(1) time)
    - distributes uniformly, doesn't cluster too much
    - deterministic (same input leads to same output)
    - Using prime numbers help reduce collisions

Dealing with Collisions
    - Seperate chaining: store multiple pieces of data in a slot
    - Linear Probing: store 1 piece of data per slot, if you get a repeat #, look for the next empty slot
*/

class HashTable {
  constructor(size = 53) {
    this.keyMap = new Array(size);
  }
  // a hash function for strings
  _hash(key) {
    let total = 0;
    let WEIRD_PRIME = 31;
    for (let i = 0; i < Math.min(key.length, 100); i++) {
      let value = key[i].charCodeAt(0) - 96;
      total = (total * WEIRD_PRIME + value) % this.keyMap.length;
    }
    return total;
  }
  set(key, val) {
    let idx = this._hash(key);
    if (this.keyMap[idx]) {
      this.keyMap[idx].push([key, val]);
    } else {
      this.keyMap[idx] = [[key, val]];
    }
    return idx;
  }
  get(key) {
    // hashes the key
    let idx = this._hash(key);
    for (let arr of this.keyMap[idx]) {
      if (arr[0] == key) {
        return arr[1];
      }
    }
    return undefined;
  }
}

let ht = new HashTable();
ht.set("pink", "#fff333");
ht.set("orange", "#aaa333");
ht.set("red", "#ppp333");
console.log(ht.get("pink"));
console.log(ht);
