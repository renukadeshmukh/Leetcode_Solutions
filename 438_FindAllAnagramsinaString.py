'''
438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's 
anagrams in s. Strings consists of lowercase English letters only and the length 
of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

'''

'''
ALGORITHM:
1. Maintain a sliding window of string S = S1 of size P and check if the 
   characters in string P are same as characters in S1

RUNTIME COMPLEXITY: O(S), where S is length of S string
SPACE COMPLEXITY: O(P) where p is the length of P string
'''

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p): return list()
        memo_s = [0] * 26
        memo_p = [0] * 26
        
        # get p's status
        for c in p:
            memo_p[ord(c) - ord('a')] += 1
        memo_p = tuple(memo_p)
        
        # initialize the sliding window
        ans = list()
        for i in range(len(p)):
            memo_s[ord(s[i]) - ord('a')] += 1
        if tuple(memo_s) == memo_p:
            ans.append(0)
        
        # slide
        for l in range(len(s) - len(p)):
            r = l + len(p)
            memo_s[ord(s[l]) - ord('a')] -= 1
            memo_s[ord(s[r]) - ord('a')] += 1
            if tuple(memo_s) == memo_p:
                ans.append(l + 1)
        return ans
            

s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))
print(s.findAnagrams("abab", "ab"))
print(s.findAnagrams("aa", "bb"))
