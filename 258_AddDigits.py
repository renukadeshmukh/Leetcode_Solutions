'''
258. Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
Since 2 has only one digit, return it.
'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = self.addAll(num)
        while sum >= 10:
            sum = self.addAll(sum)
        sum = self.addAll(sum) 
        return sum
        
    def addAll(self, num):
        q = num
        sum = 0
        rem = 0
        while q >= 10:
            rem = q % 10
            q = q / 10
            sum += rem
        sum += q
        return sum