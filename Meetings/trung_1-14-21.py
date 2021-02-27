# Return sorted array by square of value
#  inorder, preorder, postorder traversal
# [1, 5, 7, 8, -10, 10, 12]

# Input
# [-4,-1,0,3,10]
# Output
# [0,-1,3,-4,10]
# Expected
# [0,1,9,16,100]

def square_sort(sorted_arr):
  new_arr = []
  beg = 0
  end = len(sorted_arr) - 1
  while beg <= end:
    if abs(sorted_arr[beg]) > abs(sorted_arr[end]):
      new_arr.append(sorted_arr[beg])
      beg += 1
    else:
      new_arr.append(sorted_arr[end])
      end -= 1   
    
  return list(reversed(new_arr))
  
  # squared = list(map(lambda x: (abs(x),x), sorted_arr))
  # squared.sort()
  # return [val for *_, val in squared]
    
print(square_sort([-10, -8, 1, 5, 7, 10, 12]))

# def f(*args, **kwargs):
#   print(args, kwargs)
  
# f(1,2,3,4,5, a=5, b=6)


  # [0,1,1] --> [1,1,0]
  # [1,1,0] --> [1,1,0]
  # [1,0] --> [1,0]
  # return 0
  # loop thru len(students)
  # compare ith index
  # if true, pop from both
  # if not true, pop from students and append to end
  # if students = [] return 0
  # after certain iterations, if students != [], return len(students) 
  
  #
  # [1,1,0,0,1] --> [0, 0, 0, 1, 1]
  # [1, 1, 1] --> [0, 1, 1]

# heaps --> heapq
# queues ==

# time: O(N) - space: O(N)
import collections
def hungry_students(students, sandwiches):
  std = [students.count(0), students.count(1)]
  
  students = collections.deque(students)
  sandwiches = collections.deque(sandwiches)
  
  while students:
    if students[0] == sandwiches[0]:
      std[students.popleft()] -= 1
      sandwiches.popleft()
    else:
      if 0 in std:
        return len(students)
      students.rotate(-1)
  return len(students)

def hungry_students(students, sandwiches):
  wants = [students.count(0), students.count(1)]
  for sw in sandwiches: # 1
    if wants[sw]:# 1
      wants[sw] -= 1
    else:
      break
  return wants[0] or wants[1]

  
print(hungry_students([1,1,0,0], [0,1,0,1]))
print(hungry_students([1,1,1,0,0,1], [1,0,0,0,1,1]))