"""
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

stack = [l e e t c o d e]
"""
import time
def time_me(f):
  def decorate(*args, **kwargs):
    t0 = time.time()
    rv = f(*args)
    t1 = time.time()
    print(t1 - t0)
    return rv
  return decorate

@time_me
def makeGood(s):
  # iterate through string, compare each letter to the next one (test if it's the opposite case and same letter)
    # mark the indices of both, add to an array to be deleted at the end
  # keep iterating until the end
  # delete all indices from string starting at biggest index
  
  stack = []
  for c in s:
    if stack and stack[-1].lower() == c.lower() and stack[-1] != c:
        stack.pop()
        continue
    stack.append(c)
  return "".join(stack)
  
print(makeGood("leEeetcode"))

"""
You have a bomb to defuse, and your time is running out! 
Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. 
The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]
Explanation: When k is zero, the numbers are replaced by 0. 

Input: code = [2,4,9,3], k = -2
Output: [12,5,6,13]
Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. 
Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.
"""
# go vs python
# [0,1,2,3]
# list(range(4))
# [i for i in range(4)]
# [*range(4)]

def getCode(arr, k):
  # Time: O(N*k) | Space: O(N)
  if k == 0: return [0] * len(arr)
  code = []
  for i in range(len(arr)):
    val = 0
    di = 1 if k > 0 else -1
    for j in range(i + di, i + di + k, di):
      val += arr[j % len(arr)]
    code.append(val)
  return code
  # if k < 0: create new arr, append sum of last k numbers for each num

print(getCode([5,7,1,4], 3))
print(getCode([5,7,1,4], 0))
print(getCode([2,4,9,3], -2))

trung = "hello, i can't hear you"
v shape code
w
if
  if
    if
      if
        if
      else
    else
  else
else

function():
  if k = 0: return

"""
# Frontend?
# 1. Vanilla JS (ineffecient, deal with the DOM directly)
2. Frontend framework (React (the most popular by far), Vue (popular), Svelte (new, still unused in prod), Angular (was popular, mostly for legacy))
3. So many modern web apps are in React, it'll still be relevant for 5 years
  building things around React
  Next.js - react framework, let's you deal with server side rendering, image optimizations, routing
    Vercel - $60m 100
  Gatsby - react framework
    Gatsby Inc - $45m 100
React is frontend BUT a lot of people split react into front of the front end and back of the front end

Front of the front end: How things look
  building components in react
  styling them with CSS
  working on SVGs, animations (CSS)

Back of the backend:
  Routing
  dealing with APIs
  Caching
  SSR
  business logic
  Maybe node.js

TypeScript -> JavaScript + Types

.ts -> .js

React Native -> shopify is exlusively react native

React Native / Flutter: 
  learn once 
  write once

Frontend serverless
  you don't need a backend dev anymore
  2. AWS Amplify (Lambda functions)
  Lambda functions are in Node.js (for writing business logic outside your app)
  1 lambda function to do stripe authentication
  
  payment page
    enter credentials credit card, name, address
    button called 'Pay' -> trigger the stripe cloud function
  1. Firebase (noSQL database, authentication, cloud functions)

# React Context API (deal with state) <- simpler applications, MUCH easier to learn than Redux
# Redux toolkit (simplifies redux), if you want to learn redux, learn redux toolkit not redux

# React context API for UI state, external state (APIs) -> react query
# React router - main library for routing
# Component libraries - pull components (buttons, modals, nav bars) import from these libraries and use in your project
  # userful for putting a UI together quickly as opposed to making it yourself using CSS
  # react-bootstrap, material ui, bulma ui, 
  # Main weakness is, sometimes hard to customize
# Axios for dealing for APIs
# npm install axios
# npx create-react-app my-app

# React hooks basically helped react move to functional from class based
# useState hooks for local state
# useEffect hook for updating certain data on the page, especially for APIs