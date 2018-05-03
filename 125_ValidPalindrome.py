'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''
import re
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = list()
        
        for s1 in s:
            if (s1 >= '0' and s1 <= '9') or (s1 >= 'A' and s1 <= 'Z') or (s1 >= 'a' and s1 <= 'z'):  
                arr.append(s1.lower())
        print(arr)  
        return self.checkPalin(arr)
    
    def checkPalin(self, arr):
        i,j = (0, len(arr)-1)
        
        while i<j:
            if arr[i] == arr[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
    
s = Solution()
check = s.isPalindrome('A man, a plan, a canal: Panama')     
print(check)


print('c' > 'a')