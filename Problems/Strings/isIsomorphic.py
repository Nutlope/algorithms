"""
205: Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t.
"""

def isIsomorphic(self, s: str, t: str) -> bool:
    sol = {}
    for a, b in zip(s, t):
        if a in sol and b != sol[a]:
            return False
        if a not in sol and b in sol.values():
            return False
        sol[a] = b
    return True