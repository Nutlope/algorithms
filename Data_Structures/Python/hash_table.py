'''
Hash tables are key-value pairs that aren't indexed. They are dictionaries in Python
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
'''