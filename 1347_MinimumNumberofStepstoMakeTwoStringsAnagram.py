'''
1347. Minimum Number of Steps to Make Two Strings Anagram

Given two equal-size strings s and t. In one step you can choose any character 
of t and replace it with another character. Return the minimum number of steps 
to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a 
different (or the same) ordering.

Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to 
make t anagram of s.

Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 

Example 4:
Input: s = "xxyyzz", t = "xxyyzz"
Output: 0

Example 5:
Input: s = "friend", t = "family"
Output: 4

Constraints:
1 <= s.length <= 50000
s.length == t.length
s and t contain lower-case English letters only.
'''

'''
ALGORITHM:
1. Keep a dictionary to keep track of count of each character in s and t.
2. For every character in s, increment count of c in dict. 
3. For every character in t, decrement count of c in dict. 
4. Iterate over the dict. The 0-values mean s and t have equal count of that c
5. To get the answer add all positive non-zero values in dict. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

from collections import defaultdict

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sd = defaultdict(int)
        for i in range(len(s)):
            sd[s[i]] += 1
            sd[t[i]] -= 1
        
        answer = 0
        for c in sd:
            if sd[c] > 0:
                answer += sd[c]
        return answer
                
        
