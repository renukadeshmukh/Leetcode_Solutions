'''
392. Is Subsequence

Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original 
string by deleting some (can be none) of the characters without disturbing the 
relative positions of the remaining characters. (ie, "ace" is a subsequence of 
"abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you 
want to check one by one to see if T has its subsequence. In this scenario, how 
would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases. 

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
 
Constraints:
0 <= s.length <= 100
0 <= t.length <= 10^4
Both strings consists only of lowercase characters.
'''

'''
ALGORITHM:
1. Maintain 2 iterators for i, j for t and s
2. Iterate over t. 
3. If t[i] == s[j], increment j
4. If j == len(s), return True. No need to finish iteration over t. 
5. If after traversing t completely, sunsequence not found, return False

RUNTIME COMPLEXITY: O(N) where N is length of t
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if not s:
            return True
        
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
                
            if j >= len(s):
                return True
        return False