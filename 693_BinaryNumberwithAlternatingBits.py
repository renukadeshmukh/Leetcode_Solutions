'''
693. Binary Number with Alternating Bits

Given a positive integer, check whether it has alternating bits: namely, if two 
adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101

Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.

Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.

Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
'''

'''
ALGORITHM:
1. Keep checking if the last 2 bits are not the same. 

RUNTIME COMPLEXITY: O(32)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        while n > 0:
            n1 = n & 1
            n = n >> 1
            n2 = n & 1
            if n1 == n2:
                return False
        return True
            