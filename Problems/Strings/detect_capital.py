'''
Leetcode problem 520: Given a word, you need to judge whether the usage of capitals in it is right or not. We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.
'''

def detectCapitalUse(word: str) -> bool:
    # O(N) time | O(N) space

    # Create a list of 0s and 1s representing lowercase and uppercase values
    s = [0] * len(word) 
    for i in range(len(word)):
        if word[i].isupper(): 
            s[i] = 1
    
    # If first letter is uppercase and rest are lowercase or all values are either uppercase or lowercase
    return (s[0]==1 and s[1:]==[0]*(len(word)-1)) or s==[1]*len(word) or s==[0]*len(word)

# Test Cases
assert detectCapitalUse("USA") == True
assert detectCapitalUse("Nice") == True
assert detectCapitalUse("FlaG") == False
assert detectCapitalUse("ThiSis") == False