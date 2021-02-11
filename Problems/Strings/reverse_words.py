'''
Leetcode problem 557: Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
'''

def reverseWords(s: str) -> str:
    # O(N^2) time | O(N) space

    # Split the sentence into words
    lst = s.split()

    for i in range(len(lst)):
        # for each word, reverse it by splicing
        lst[i] = lst[i][::-1]
    return " ".join(lst)

# Test Cases
assert reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
assert reverseWords("How dare you man!") == "woH erad uoy !nam"