# This outlines the main techniques for solving each data structure

## Array

- Two pointer technique: start two pointers, one pointing to the beginning of the array and one pointing to the end. While they don't cross, do logic and increment/decrement them appropriately
- Sliding window technique: O(N) solution to getting the max/min of a consecutive subarray in an array
- Use sets/dicts to check if a value is in an array (O(1) vs O(N))
- 3 pointer problem: for loop through a sorted array, then use 2 pointers
- 2D arrays
  - bitwise XOR with 1 to invert (val^1)
  - union find data structure
- Optimizations
  - Write/delete values from the back of the array when possible to save on time complexity, like stack
  - If you need to delete values from front, consider overwriting them with 0 or -1 instead of popping

## String

- Two pointer technique
- Unicode manipulation: using ord() and chr() to go from char to unicode and unicode to char respectively. Used in problems where we want to use the alphabet.
- Finding palindromes: treat each letter as the center of a palindrome, and use two pointers on the outside to check
