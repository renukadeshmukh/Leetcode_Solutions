'''
387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's 
index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

'''
ALGORITHM:
1. Count occurance of each character in s
2. Iterate over s and find the first char from left with count = 1. 
3. Return such an index. If no index is found, return -1. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

from collections import defaultdict
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dd = defaultdict(int)
        for c in s:
            dd[c] += 1
            
        for i,c in enumerate(s):
            if dd[c] == 1:
                return i
        return -1
        