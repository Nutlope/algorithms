from typing import List  # Import for static type checking

'''
Leetcode problem 344: Write a function that reverses a string inplace. The input string is given as an array of characters char[].
'''

# Solution 1: Two pointer technique
def reverseString(s: List[str]) -> List[str]:
    # O(N) time | O(1) space
    l = 0
    r = len(s) - 1
    
    # swap pointers at the beginning and end, then increment/decrement them
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    return s

# Solution 2: Built-in reverse method
def reverseString2(s: List[str]) -> List[str]:
    # O(N) time | O(1) space
    s.reverse()
    return s

# Test Cases
assert reverseString(["h","e","l","l","o"]) == ["o","l","l","e","h"]
assert reverseString(["H","a","n","n","a","h"]) == ["h","a","n","n","a","H"]
assert reverseString2(["h","e","l","l","o"]) == ["o","l","l","e","h"]
assert reverseString2(["H","a","n","n","a","h"]) == ["h","a","n","n","a","H"]