'''
Leetcode problem 557: Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
'''

def reverseVowels(s: str) -> str:
    # O(N) time, O(N) space

    # Use a set for because checking if an element is in a set is O(1) on average
    vowels = set(list('aeiouAEIOU'))
    l = 0
    r = len(s) - 1
    s = list(s)
    # 2 pointer approach
    while l < r: 
        if s[l] not in vowels:
            l += 1
        elif s[r] not in vowels:
            r -= 1
        else:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    return "".join(s) 

# Test Cases
assert reverseVowels("hello") == "holle"
assert reverseVowels("leetcode") == "leotcede"
assert reverseVowels("Ello") == "ollE"