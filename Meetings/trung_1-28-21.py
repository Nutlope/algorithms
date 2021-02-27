"""
# You are given an array people where people[i] is the weight of the ith person, 
# and an infinite number of boats where each boat can carry a maximum weight of limit. 
# Each boat carries at most two people at the same time, 
# provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.

people = [1,2], limit = 3 => 1
people = [3,2,2,1], limit = 3 => 3
people = [3,5,3,4], limit = 5 => 4
1,1,2,2 ; 3 => 2, 3
1,2,3 ; 3 => 

[1,2,2,3], limit=3 => 3
Q: if the weight of every person is greater than the limit, what should I return?
"""
# boat variable, 2 pointers start and end
# Sort people [1,1,2,2] limit = 3
# Take num at start, check if it's equal to the limit. If it is, boat++ and start++
# If it's not equal, check if the num at start + num at end is equal to or less than the limit. if it is equal, boat++, start++, end--
# if it's not, boat++, end--
# keep going until start > end
# return boat
# [3,3,3,3]

# greedy: 
    # local: given an array, send 1 person away
# O(nlogn) time complexity and O(1) space complexity
def minBoats(people, limit):
    people.sort()
    start = boat = 0
    end = len(people) - 1
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        boat += 1
    return boat

print(minBoats([3,5,3,4], 5))