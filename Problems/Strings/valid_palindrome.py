'''
Leetcode problem 125: Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases. For the purpose of this problem, we define empty string as valid palindrome.
'''

# Solution 1 - Simple Solution
def isPalindrome(s: str) -> bool:
    # O(N^2) time | O(N) space
    if s == "":
        return True
    s_cleaned = ""
    for char in s:
        # make new str with only lowercase alphanumerics
        if char.isalnum():
            s_cleaned += char.lower()
    
    # check if it's equal to the reverse
    return s_cleaned == s_cleaned[::-1]

# Solution 2 - In place using 2 pointer approach
def isPalindromeInplace(s: str) -> bool:
    # # O(N^2) time | O(N) space
    l = 0
    r = len(s) - 1
    
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            if not s[l].lower() == s[r].lower():
                return False
            l += 1
            r -= 1
    return True

# Test Cases
assert isPalindrome("A man, a plan, a canal: Panama") == True
assert isPalindrome("race a car") == False
assert isPalindromeInplace("A man, a plan, a canal: Panama") == True
assert isPalindromeInplace("race a car") == False