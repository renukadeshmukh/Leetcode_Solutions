'''
263. Ugly Number

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
'''

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        isUgly = False
        while True:
            if num == 1:
                isUgly = True
                break
            if num%2 == 0:
                num = num/2
                continue
            elif num%3 == 0:
                num = num/3
                continue
            elif num%5 == 0:
                num = num/5
                continue
            else:
                break
        return isUgly
            
        
