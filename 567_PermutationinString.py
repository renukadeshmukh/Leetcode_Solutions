'''
567. Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the 
permutation of s1. In other words, one of the first string's permutations is the 
substring of the second string. 

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''

'''
ALGORITHM : Sliding Window
1. Save counts of each character in s1 in an array of length 26 -> d_s1. 
2. For every chunk of length l1 in s2, in a similar array -> d_s2
3. Compare if d_s1 == d_s2. If yes, then return true.
4. Else slide the window to right by one and update the array d_s2 and adding 
   next character to d_s2 and substracting the character just left behind by the
   sliding window


RUNTIME COMPLEXITY: O(l1 + l2) where l1 and l2 are lengths of s1 and s2
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1=="":
            return True
        if len(s1) > len(s2):
            return False
        
        d_s1 = [0 for i in range(26)]
        for c in s1:
            d_s1[ord(c)-97] += 1
        
        d_s2 = [0 for i in range(26)]
        for i in range(len(s1)):
            d_s2[ord(s2[i])-97] += 1                  
        if d_s1 == d_s2:
            return True
        
        for i in range(len(s1),len(s2)):
            d_s2[ord(s2[i-len(s1)])-97] -=1
            d_s2[ord(s2[i])-97] +=1
            
            if d_s1 == d_s2:
                return True 
      
        return False
        
        
        
s = Solution()
print(s.checkInclusion("adc", "dcda"))
print(s.checkInclusion("ab","eidbaooo"))