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