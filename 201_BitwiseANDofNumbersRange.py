'''
201. Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of 
all numbers in this range, inclusive.

Example 1:
Input: [5,7]
Output: 4

Example 2:
Input: [0,1]
Output: 0
'''

'''
ALGORITHM:
The bitwise AND of the range [M,N] is keeping the common bits of m and n from 
left to right until the first bit that they are different, padding zeros for the 
rest.

RUNTIME COMPLEXITY: O(32) = O(1)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while m != n:
            m = m >> 1
            n = n >> 1
            i += 1
        return m << i