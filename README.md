# Data Structures and Algorithms

This repository is for me to document my knowledge on common data structures and algorithms. Information is from Elements of Programming Interviews, Leetcode and Colt Steele's 'Javascript Algorithms and Data Structures' course.

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

## Problem Solving Approach

**1. Understand the problem**

- Make sure you can restate it in your own words
- Inputs and outputs of the problem
- Do I have enough info to solve the problem?
- How do I label important pieces of data?

**2. Explore Concrete Examples**

- Start exploring simple examples
- Progress to complex examples
- Explore examples with empty / invalid inputs

**3. Break it Down**

- Explicitly write down the steps you need to take

**4. Solve & Simplify**

- Find the core difficulty
- Temporarily ignore it and write a simplified version
- Incorporate core difficulty into your solution

**5. Look back and refactor**

- Can you check the result?
- Can you derive the result differently?
- Can you understand it at a glance?
- Can you improve the performance?
- Other ways to refactor?
- How have others solved this problem?
