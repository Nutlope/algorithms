# Welcome to the Coding Interview - You Suck

These are my key takeaways from this [guide](https://docs.google.com/document/d/1eKirumpmwDWTtKCJKn2HuoQ2NavEfR41whmTyaQcio4/edit#).

- I'm at a beginner level right now because I don't even know all the basic data structures yet (still missing Sorting, Recursion, Dp, Graphs, and Greedy Algorithms)
- It takes a long time to really understand data structures well, 200+ leetcode questions
- It's not a game of luck, it's mostly a game of practice
- Deliberate and consistent practice is how people become good at something.
- Play the long game. I'm going to be interviewing in now and later this year, make sure I'm 200% ready for August and use interviews in March-June as practice.

### Reasons why someone would suck
- Approach is not consistent
- You're practicing incorrectly
- You're not fast enough

## How to get good
- Focus on one topic at a time, drill down on it until you really know it
- Don't worry about repeating problems, if you don't understand do them again and again

### Decode the usage of each DS & Algo
- Understand the DS or algo to the point where you can implement off the top of your head
- Derive rules for when to use diff things? I.e, mergesort when O(N^2) is not tolerated and there's lots of memory
- Backtest those rules and understand when they don't work
- Understand what happens when you improperly apply an algorithm

### General Approach

1. Look at the characteristics in the problem. Can you combine a sufficient number of these characteristics and match them to a known data structure/algorithm? 
2. Generate a few examples. What are the patterns generated from the examples? What will the algorithm look like?
3. Look at every substep of the algorithm. For every substep, go back to step 1 with the question “how can I optimize this substep?”

To help you better optimize your solution, here is the order of precedence. If you end up with an algorithm of a particular time complexity, your more optimal solution must be an operation below it:

O(2N , 3N): Permutation
O(N2 , N3…): recursion/generate subsets, nested loops
O(N log N) : Sorting/heap
O(N) : Iteration, pointers/sliding window, common array operations
O(log N) : Binary Search/ Exponentially sized steps search

If going down the list is not applicable or possible, consider combining operations or setting up preconditions such that some steps are no longer needed.

For instance, if you find your solution or part of your solution is N2, then you should try sorting, iterating, doing a binary search, or some combination thereof to improve your solution.