'''
A tree structure, where the parent is always bigger than the children for a max binary heap
Two values max under each node. Left children are filled up first. Evenly distributed
Binary Heaps are mostly used for priority queues
Can implement binary heap with array. children are at 2n + 1 for L and 2n + 2 where n is index of parent
2 variations: Max Binary Heap or Min Binary Heap
BIG O: O(log N) insertion and removal, O(N) search

Also referred to as a priority queue. Data structure where each element has a priority. Elements with high priorities are served before elements with low priorities. Can be implemented using a binary heap
'''
import heapq as heap
# for a heap, children are at 2n + 1 for L and 2n + 2 where n is index of parent
# Min Binary Heap by default, if we want max, invert values
L = []

# pushes heap into array and organizes
heap.heappush(L,20)
heap.heappush(L,10)
heap.heappush(L,2)
heap.heappush(L,52)
heap.heappush(L,32)

print(L)
heap.heappop(L) # pops the root
print(L)

L1 = heap.nsmallest(4,L) # returns 4 smallest #s
L1 = heap.nlargest(4,L) # returns 4 largest #s
# print(L1)

list1 = [4, 4, 4, 6, 66, 91]
heap.heapify(list1) # turns a list into a heap
print(list1)