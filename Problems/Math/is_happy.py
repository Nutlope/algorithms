'''
Leetcode problem 202: Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''
from math import floor

def isHappy(n: int) -> bool:
    # Solution 1 - O(N^2) time | O(N) space
    visited = set()
    while n != 1:
        x, n = n, 0
        while x != 0:
            n += (x % 10) ** 2
            x = floor(x/10)
        if n in visited: 
            return False
        visited.add(n)
    return True

def isHappyRecursive(n: int) -> bool:
    # Solution 2 - Using Recursion - O(N^2) time | O(N) space
    visited = set()
    def recursiveFunc(n):
        intLst = list(str(n))
        total = 0
        for num in intLst: total += int(num)**2
        if total == 1: return True
        if total in visited: return False
        visited.add(total)
        return recursiveFunc(total)
    return recursiveFunc(n)

# Test Cases
assert isHappy(19) == True
assert isHappy(2) == False
assert isHappyRecursive(19) == True
assert isHappyRecursive(2) == False