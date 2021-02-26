"""
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:
Biggest reason for sorting an array is searching.

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Sample Input: 

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 
target = 14

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 
target = 20

Hint: O(RlogC) O(ClogR)  O(R + C) (2 ptrs)

Brute force, 2 for loops search for that val, and return true/false
O(N^2) time | O(1) space
def findValinMatrix(matrix, target):
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == target:
        return True
  return False
  
print(findValinMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 55))

def findVal(matrix, target):
  for i in range(len(matrix)):
    left = 0
    r = len(matrix)-1
    
    while left < r:
      if matrix[left] == target or martix[right] == target:
        return True
      if matrix[left] < target:
        left += 1
      if matrix[right] > target:
        right -= 1
        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        r = 0; c = C - 1
        while r < R and c >= 0:
            if matrix[r][c] == target: return True
            elif matrix[r][c] < target: 
                r += 1
            else: 
                c -= 1
        return False
        
")()()()()())(" => False
"()((())())" => True

")(" 

"(" == ")"
")"
Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

"([)]"
"([])"

"(*))" => valid


784. Letter Case Permutation
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.


Example 1:
Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
Input: S = "3z4"
Output: ["3z4","3Z4"]

Example 3:
Input: S = "12345"
Output: ["12345"]

Example 4:
Input: S = "0"
Output: ["0"]
"""
def letterPermutation(S):
  ans = [""]
  for c in S.lower():
    nxt_ans = []
    for prev in ans:
      nxt_ans.append(prev + c)
      if c.isalpha(): 
        nxt_ans.append(prev + c.upper())
    ans = nxt_ans
  return ans
  
def letterPermutation(S):
  # 2^n space | O(N^3) time
  # String addition is O(n)
  # O(N * 2^N) 
  sol = []
  isOdd = True
  for char in S:
    if char.isalpha():
      if sol == []:
        sol.append(char.lower())
        sol.append(char.upper())
        continue
      sol = sol * 2
      for i in range(len(sol)):
        if isOdd:
          sol[i] += char.lower()
          isOdd = False
        else:
          sol[i] += char.upper()
          isOdd = True
    else:
      if sol:
        for i in range(len(sol)):
          sol[i] += char
      else:
        sol.append(char)
  return sol

print(letterPermutation("a1b2"))
print(letterPermutation("3z4"))
print(letterPermutation("12345"))
print(letterPermutation("0"))
print(letterPermutation("aaaa")) 
# assert set(letterPermutation("a1b2")) == set(["a1b2","a1B2","A1b2","A1B2"])
# assert letterPermutation("3z4") == ["3z4","3Z4"]
# assert letterPermutation("12345") == ["12345"]
# assert letterPermutation("0") == ["0"]
  
  # all possible scenarios so for 'aaa" -> Aaa AAa AAA, aAa 
  # "a" -> "" + "a", "" + "A"
  # "a" -> ["a", "A"]
    #  b      "ab" "aB" "Ab" "AB"
    #  3      "ab3" "Ab3" ... ...
    #  c      "ab3c" "ab3C" ...
  # "a" -> a, A
  # "a" -> [aa, Aa, a, A]
  
# PROBLEM 
# Valid parenths

# PROBLEM 20
def isValid(parans):
  # { }
  # ( )
  # [ ]
  stack = []
  s = {'(': ')', '[': ']', "{": "}"}
  for char in parans:
    stack.append(char)
    if s[stack[-2]] == stack[-1]:
      del stack[-2:]
  return stack == []
  
  stack = []
  s = {'(': ')', '[': ']', "{": "}"}
  for char in parans:
    if c in "[{(":
      stack.append(char)
    elif s[stack[-1]] == c:
      stack.pop()
  return stack == []
  

def f(S):
  op = 0
  for c in S:
    op += 1 if c == "(" else -1
    if op < 0: return False
  return op == 0