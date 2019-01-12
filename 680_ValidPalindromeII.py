'''
680. Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether 
you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''

'''
ALGORITHM:
1. i = 0, j = len(S) -1
2. while S[i] == S[j], inc i and dec j
3. remove i-th character and check if rest of the string is palindrome
4. remove j-th character and check if rest of the string is palindrome
5. if either is palindrome, return True, else return False 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def validPalindrome(self, S):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(S)-1
        while i <= j and S[i] == S[j]:
            i += 1
            j -= 1
            
        if i >= j:
            return True
        else:
            return (S[i:j] == S[i:j][::-1]) or (S[i+1:j+1] == S[i+1:j+1][::-1])
        
