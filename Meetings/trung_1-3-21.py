# Time complexity: O(W*N) - Space complexity: O(M) W is width of the wall. N is number of rows. M is numbers of total bricks
import collections
def returnLine(arr):
    freq = collections.defaultdict(int)
    for row in arr:
        prefix = 0
        for val in row:
            prefix += val
            freq[prefix] += 1
        
            
    freq[sum(arr[0])] = 0
    return len(arr) - max(freq.values())
def returnLine1(nestedList):
    new_arr = []
    big_set = set()
    for row in nestedList:
        new_row = set()
        s = 0
        for val in row[:-1]:
            s += val
            new_row.add(s)
            big_set.add(s)
        new_arr.append(new_row)
    
    # {1,2,3,4}
    # {1,2,3,4}
    # {1,2,3,4}
    # ...
    # {1,2,3,4} 
    # 10000 rows, for each index , it check for 10000 times
    # optimal: for 10000 row, for {1,2,3,4}, freq[prefix] += 1
    
    min_crossed = len(nestedList)
    for index in big_set: # {1,2,3,4}
        crossed = sum(index not in row for row in new_arr)
        min_crossed = min(min_crossed, crossed)
    return min_crossed

print(returnLine1([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))
print(returnLine1([[1]]))
print(returnLine1([[1],[1]]))
print(returnLine1([[1,1],[2],[1,1]]))
print(returnLine1([[10000,10000],[10000,10000],[10000,10000]]))
print(returnLine1([[10**9] * 1000 for _ in range(200)]))
# [1,1]
# [2]
# [1,1]
# Input - [[1,1],[2],[1,1]]