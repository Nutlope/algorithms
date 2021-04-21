arr = [1,14,6,2,73,13,64,21]

# Input: arr = [1,14,6,2,73,13,64,21], k = 3
# Output: 150

# Normal way - O(N^2)
def maxSum(arr, k):
    theSum = 0
    largestSum = 0
    for i in range(len(arr)-k+1):
        for j in range(i, i+k):
            theSum += arr[j]
        largestSum = max(theSum, largestSum)
        theSum = 0
    return largestSum

print(maxSum(arr, 3))

# Sliding method approach - O(N)
def optimalMaxSum(arr,k):
    theSum, largestSum = 0, 0
    # calculate first sliding window
    for i in range(k): theSum += arr[i]
    largestSum = theSum

    for i in range(k, len(arr)-1):
        theSum += arr[i] - arr[i-k]
        if theSum > largestSum:
            largestSum = theSum
    return largestSum

print(optimalMaxSum(arr, 3))