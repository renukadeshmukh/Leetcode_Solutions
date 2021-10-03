'''
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common 
subsequence.

A subsequence of a string is a new string generated from the original string with 
some characters(can be none) deleted without changing the relative order of the 
remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). 
A common subsequence of two strings is a subsequence that is common to both 
strings. 

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:
1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
'''

'''
ALGORITHM:
1. If text1[i] == text2[j], then dp[i][j] = dp[i-1][j-1] + 1.
2. Else dp[i][j] = maximum(dp[i-1][j] , dp[i][j-1]).

RUNTIME COMPLEXITY: O( M*N )
SPACE COMPLEXITY: O( M*N )
'''

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1) 
        n = len(text2) 

        store = [[0]*(n+1) for i in xrange(m+1)] 

        for i in range(m+1): 
            for j in range(n+1): 
                if i == 0 or j == 0 : 
                    store[i][j] = 0
                elif text1[i-1] == text2[j-1]: 
                    store[i][j] = store[i-1][j-1]+1
                else: 
                    store[i][j] = max(store[i-1][j] , store[i][j-1]) 
        return store[m][n]