from typing import List  # Import for static type checking

'''
Leetcode problem 728: A self-dividing number is a number that is divisible by every digit it contains. For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero. Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
'''

def selfDividingNumbers(left: int, right: int) -> List[int]:
    sol = []
    for num in range(left, right+1):
        # set a boolean value, check conditions and if any are false set boolean to false
        isDividable = True
        for digit in str(num):
            if int(digit) == 0 or int(num) % int(digit) != 0:
                isDividable = False
        # only add num to sol array if all conditions are true
        if isDividable: sol.append(num)
    
    return sol

# Test Cases
assert selfDividingNumbers(1,22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
assert selfDividingNumbers(1,100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22, 24, 33, 36, 44, 48, 55, 66, 77, 88, 99]