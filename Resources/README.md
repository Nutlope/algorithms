# Resources for coding interviews

These are a list of my favorite resources for coding interviews as well as my notes from them.

## Big O Notation

Measures the performance of an algorithm, both in terms of how long it will take (time complexity) and how much memory it uses (space complexity).

### Time Complexity

A way to talk about how the worst-case scenario runtime of an algorithm changes as the input grows.

Different types (best to worst) - put in a graph here

- O(1) does not depend on input
- O(log n)
- O(n) depends on the input linearly
- O(nlog n)
- O(n^2), runtime is proportional to n squared - can be a O(n) inside an O(n)

Rules / Useful

- Constants don't matter
- Arithmetic operations and var assignments are constant
- Accessing elements in an array/object is constant
- For a loop, complexity is length of the loop \* complexity of what's inside the loop

### Space Complexity

Auxiliary space complexity is what happens in the algorithm not worrying about inputs (which we assume will be increasing anyway)

Rules of Thumb

- Most primitaves are constant space (numbers, undefined, ect...)
- Strings/Arrays/Objects require O(n) space (n is number of elements)

### Object & Array Performance

- Objects have O(1) access, intertion, and removal, and O(N) searching.
- They have O(N) for Object methods like .keys, .values, and .entries
- Arrays O(1) access, O(N) search, and intertion/removal depends on where
