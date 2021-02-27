"""
# Met 3 times before for JS. Did these problems: 1512, 1544, 877

1513.

Given a binary string s (a string consisting only of '0' and '1's).
Return the number of substrings with all characters 1's.
Since the answer may be too large, return it modulo 10^9 + 7.


s = "0110111"
=> 9
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.

1. Count the number of 1s 
2. Find the longest consequetive list of 1s and assign to var cons 
3. Count the number of times they appear 2 in a row, ... cons in a row 
4. Add them all up and return that number

1. convert Python
2. make it clean
3. pythonic
4. optimal solution

1. go through s:
2. determind the length of consecutive 1s
    for each: apply f(n) => result
4. sum them up

s = "111 000000 111111111 0"
 000 11111111 0 1"
    3 
    f(n)
    result
    
(n + 1) * n / 2

def binary_search(target, array):
  pass

"""
  s += '0'
  sequence = result = 0
  for first, second in zip(s, s[1:]):
    if first == second == '1':
      sequence += 1
    elif first == '1' and second == '0':
      result += (sequence + 2) * (sequence + 1) // 2 
      sequence = 0
    elif first == '0' and second == '1':
      sequence = 0
  return result % (10**9 + 7)
    
# O(N^3), O(1)
# O(N). Space: O(1)
def substringCounter(s):
  longest = sequence = 0
  for first, second in zip(s, s[1:]):
    if first == second == '1':
      sequence += 1
    else:
      sequence = 0
    longest = max(longest, sequence)
  longest += 1
  
  counter = 0
  for length in range(1, longest + 1):
    sub = "1" * length
    for times in range(len(s)):
      if s[times : length + times] == sub: # O(N)
        counter += 1
  
  return counter % (10**9 + 7)
  
print(substringCounter("0110111"))
print(substringCounter("1111111111"))
print(optimal_counter("0110111"))
print(optimal_counter("1111111111")