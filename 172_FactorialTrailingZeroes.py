'''
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
'''

'''
ALGORITHM:
1. All trailing 0 is from factors 5 * 2.

But sometimes one number may have several 5 factors, for example, 25 have two 5 
factors, 125 have three 5 factors. In the n! operation, factors 2 is always ample. 
So we just count how many 5 factors in all number from 1 to n.

RUNTIME COMPLEXITY: O(log(N,5)) n to base 5
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n >= 5:
            n = n/5
            cnt += n
        return cnt