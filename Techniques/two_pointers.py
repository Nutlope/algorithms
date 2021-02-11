arr = [2,5,1,8]

def twoPointers(arr):
    l = 0
    r = len(arr) - 1

    while l < r:
        # do something, if statement
        # swap for example
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    return arr # return something