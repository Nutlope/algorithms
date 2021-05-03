# Recursion is a process that calls itself
# Uses: DOM/tree/graph traversal, JSON.stringify
# 2 essential parts for recursive function: Base case and different input for each function revokal
# Base case is when the recursion ends

def isEven(some_lst):
    # Recursive function to check if items in a list are all even
    if some_lst == []:
        return True

    first = some_lst.pop(0)
    if first % 2 != 0:
        return False
    return isEven(some_lst)

# print(isEven([22, 64, 43, 45]))

def countDown(num):
    if num <= 0:
        print("All done!")
        return
    print(num)
    num -= 1
    countDown(num)

# print(countDown(3))

def factorial(num):
    if num == 1: return 1
    return num * factorial(num-1)

print(factorial(3))

def power(base, exponent):
  if exponent == 0:
    return 1
  else:
    return base * power(base, exponent - 1)

print(power(2, 3))

"""
How does this function work?

1. Add console.log to call stack

2. Add power(2,3) to call stack
3. Execute power(2,3) which returns 2 * power(2,2)

4. Add 2 * power(2,2) to call stack
5. Execute 2 * power(2,2) which returns 2 * 2 * power(2,1)

6. Add 4 * power(2,1) to call stack
7. Execute 4 * power(2,1) which returns 4 * 2 * power(2,0)

8. Add 8 * power(2,0) to call stack
9. Execute 8 * power(2,0) which returns 8 * 1

10. Pop power(2,0) off call stack
11. Pop power(2,1) off call stack
12. Pop power(2,2) off call stack
13. Pop power(2,3) off call stack

14. Execute console.log(8) and pop off call stack
"""
