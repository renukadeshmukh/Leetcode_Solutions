'''
482. License Key Formatting

You are given a license key represented as a string S which consists only alphanumeric character and dashes. 
The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, 
except for the first group which could be shorter than K, but still must contain at least one character. 
Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted 
to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4
Output: "5F3Z-2E9W"

Example 2:
Input: S = "2-5g-3-J", K = 2
Output: "2-5G-3J"

Note:
The length of string S will not exceed 12,000, and K is a positive integer.
String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
String S is non-empty.
'''

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        res2 = []
        S = "".join(S.split("-")).upper()
        if len(S) <= K:
            return S
        
        i, limit = -1,len(S) * -1
        while i >= limit:
            res2.append(S[i])
            if i % K == 0:
                res2.append('-')
            i -= 1
        
        if res2[-1] == '-':
            res2 = res2[:-1]
        return ''.join(reversed(res2))
            


s = Solution()
res = s.licenseKeyFormatting('5F3Z-2e-9-w', 4)
print(res)

res = s.licenseKeyFormatting('2-5g-3-J', 2)
print(res)
