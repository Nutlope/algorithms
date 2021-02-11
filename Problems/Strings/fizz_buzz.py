from typing import List  # Import for static type checking

'''
Leetcode problem 412: Write a program that outputs the string representation of numbers from 1 to n. But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
'''

def fizzBuzz(n: int) -> List[str]:
    # O(N) time | O(N) space
    arr = []
    for num in range(1, n+1):
        # define string, add values to it depending on problem requirements
        thestr=""
        if num % 3 == 0:
            thestr += "Fizz"
        if num % 5 == 0:
            thestr += "Buzz"
        # if num is not divisible by 3 or 5, we want to return the number itself as a string
        if not thestr:
            thestr = str(num)
        arr.append(thestr)
    return arr

# Test Cases
assert fizzBuzz(15) == [
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]