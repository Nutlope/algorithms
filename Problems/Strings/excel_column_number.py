'''
Leetcode problem 412: Write a program that outputs the string representation of numbers from 1 to n. But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

My Notes: This question is pretty much a conversion from a base 26 number into a base 10 number. For a sample input ABC, where the letter A starts at 1 and works up, just solve like I'm converting to binary (except instead of base 2 it's base 26)
'''

def titleToNumber(s: str) -> int:
    # O(N) time | O(1) space
    total = 0
    # Iterate through and follow base 26 -> base 10 conversion
    for idx, char in enumerate(s):
        total += (ord(char) - ord('A') + 1) * 26 ** (len(s) - idx - 1)
    return total

# Test Cases
assert titleToNumber('J') == 10 # 10 * 26**0 = 10
assert titleToNumber('BB') == 54 # (2 * 26**0) + (2 * 26**1) = 54
assert titleToNumber('ABC') == 731 # 3 * 26**0 + 2 * 26**1 + 1 * 26**2 = 731
assert titleToNumber('AAAA') == 18279 # (1 * 26**0) + (1 * 26**1) + (1 * 26**2) + (1 * 26**3) = 18279
