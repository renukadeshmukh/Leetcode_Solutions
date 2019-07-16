'''
1071. Greatest Common Divisor of Strings

For strings S and T, we say "T divides S" if and only if S = T + ... + T  
(T concatenated with itself 1 or more times)
Return the largest string X such that X divides str1 and X divides str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Note:
1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.
'''

'''
ALGORITHM:
1. For length of str1 and str2 find common factors.
2. For each common factor x, check if s[:x] is a valid substring
   for both str1 or str2

RUNTIME COMPLEXITY: O(MN) where m,n = length of str1 and str2
SPACE COMPLEXITY: O(Mk + Nk) for k common factors
'''

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        common_factors = self.factors(str1, str2)
        mx = 0
        for i in common_factors:
            s = str1[:i]
            if str1 == s * (len(str1)//i) and str2 == s * (len(str2)//i) and len(s) > mx:
                mx = i
            
        return str1[:mx]
        
        
    def factors(self, s1, s2):
        ln1, ln2 = len(s1), len(s2)
        min_len = min(ln1, ln2)
        factors = set()
        for i in range(1, min_len+1):
            if ln1 % i == 0 and ln2 % i == 0:
                factors.add(i)

        return factors

s = Solution()
print(s.gcdOfStrings("ABCABC", "ABC"))
print(s.gcdOfStrings("ABABAB", "AB"))
print(s.gcdOfStrings("LEET", "CODE"))
