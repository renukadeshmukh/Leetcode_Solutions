'''
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
'''

class Solution(object):
    '''
    The answer lies in the fibonacci sequence
    '''
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = 1
        
        while n > 0:
            #c = b
            b = a + b
            a = b - a
            n -= 1
        return b
        
