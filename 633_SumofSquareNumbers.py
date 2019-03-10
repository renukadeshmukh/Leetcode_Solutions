'''
633. Sum of Square Numbers

Given a non-negative integer c, your task is to decide whether there're two 
integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 
Example 2:
Input: 3
Output: False
'''

'''
ALGORITHM:
1. a = 0 and b = sqrt(c)+1
2. while a < b, keep checking if a^2 + b^2 = c
3. If yes, return True
4. If a^2 + b^2 < c, increment a by 1, else decrement b by 1
 
RUNTIME COMPLEXITY: O(SQRT(C))
SPACE COMPLEXITY: O(1)
'''

from math import sqrt
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        r = int(sqrt(c)) + 1
        a,b = 0,r
        
        while a <= b:
            c1 = a*a + b*b
            if c1 == c:
                return True
            elif c1 < c:
                a += 1
            else:
                b -= 1
        return False