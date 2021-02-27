""
is vs ==
-5 256

DFS stack, BFS queue

hash map, heap (medium light - medium heavy)

https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/      
https://leetcode.com/problems/top-k-frequent-words/description/                 

https://leetcode.com/problems/the-skyline-problem/
https://leetcode.com/problems/simplify-path/

map hash dict, set

[72, 68, 45, 89, 90, 91, 45, 46, 47, 48, 49, 41, 40]

output:
return the nearest day (in the past) that has higher temperature

Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.

Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

"""
== vs is
id()
if val is None
# 5 == '5' YES
# 5 === '5' NO

def isIsomorphic(self, s: str, t: str) -> bool:
    return list(map(s.find, s)) == list(map(t.find, t))
    
def isIsomorphic(self, s: str, t: str) -> bool:
    return len(set(zip(s,t))) == len(set(s)) == len(set(t))
    
def isIsomorphic(s, t):
    # if len(s) != len(t):
    relation = {}
    for c1, c2 in zip(s, t):
        if c1 in relation and relation[c1] != c2:
            return False
        if c1 not in relation and c2 in relation.values():
            return False
        relation[c1] = c2
    return True
    
    new_dict = {}
    for i in range(len(s)):
        if s[i] not in new_dict:
            if t[i] in new_dict.values(): # O(1)
                return False 
            new_dict[s[i]] = t[i]
        else:
            if new_dict.get(s[i]) == t[i]:
                continue
            else:
                return False
    return True
print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))