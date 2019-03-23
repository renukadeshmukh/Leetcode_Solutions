'''
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
'''

'''
ALGORITHM:
1. Divide and Conquer

RUNTIME COMPLEXITY: O(LOG(N))
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        npos = abs(n)
        
        power = self.myPowRecursive(x, npos)
        if n < 0:
            return 1/power
        return power
    
    def myPowRecursive(self, x, npos):
        if npos == 0:
            return 1
        if npos == 1:
            return x
        elif npos % 2 == 0:
            p = self.myPowRecursive(x, npos/2)
            return p * p
        else:
            p = self.myPowRecursive(x, (npos-1)/2)
            return p * p * x