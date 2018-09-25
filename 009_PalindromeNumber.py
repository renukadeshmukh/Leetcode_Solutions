'''
9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        len = 0
        y = x
        while y>9:
            y = y / 10
            len += 1
        flag = True
        while x>0 :
            last = x % 10
            first = x / (10 ** len)
            if last != first:
                return False
            else:
                x = x - (first * (10 ** len))
                x = x / 10
                len -= 2
        return True
    

            
        

