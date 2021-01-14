# Recursion is a process that calls itself
# Uses: DOM/tree/graph traversal, JSON.stringify

# Resurive function to check if items in a list are all even

def isEven(some_lst):
    if some_lst == []:
        print("doesn't exist no mo")
        return True

    if len(some_lst):
        first = some_lst.pop(0)
        print(some_lst)
        if first % 2 != 0:
            return False
        isEven(some_lst)

print(isEven([22, 64, 42, 45]))