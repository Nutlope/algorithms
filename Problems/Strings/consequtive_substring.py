# 1513.

# Given a binary string s (a string consisting only of '0' and '1's).
# Return the number of substrings with all characters 1's.
# Since the answer may be too large, return it modulo 10^9 + 7.

# s = "0110111"
# => 9

# "1" -> 5 times.
# "11" -> 3 times.
# "111" -> 1 time.

# count = 4 + 3 + 2 + 1
# s = "1111"

# search consequtive 1s, consequtive 2s, ect until none are found

# PSUEDOCODE
# define count variable = 0, length = 1
# while length <= len(s):
    # loop thru and check how many substrings with length L
    # add this number to a local var
    # If local var == 0: break. If not, add to count var, increment length

def subStrings(s):
    count = 0
    l = 1
    while l <= len(s):
        iCount = 0
        for i in range(len(s)):
            if s[i:i+l] == "1"*l:
                iCount += 1
        if iCount == 0:
            break
        count += iCount
        l += 1
    
    return count

s = "0110111"
print(subStrings(s))