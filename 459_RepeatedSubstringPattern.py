'''
459. Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of 
it and appending multiple copies of the substring together. You may assume the 
given string consists of lowercase English letters only and its length will not 
exceed 10000. 

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"
Output: False

Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" 
twice.)
'''

'''
ALGORITHM:
1. ln = len(S)
2. Find all factors of of ln
3. Generate strings of length ln by taking substring of size = factors of ln
and check if these generated strings are same as s.

RUNTIME COMPLEXITY: O(N * Sqrt N)
SPACE COMPLEXITY: O(N)
'''

from math import sqrt
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False
        
        ln = len(s)
        
        r = int(sqrt(ln) + 1) 
        for i in range(1 , r):
            if ln % i == 0:
                x,y = i, ln/i
                if x != ln and s[0:x] * y == s:
                    return True
                if y != ln and s[0:y] * x == s:
                    return True
        return False
