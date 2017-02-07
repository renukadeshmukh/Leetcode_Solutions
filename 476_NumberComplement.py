'''
476. Number Complement

Given a positive integer, output its complement number. The complement strategy is to 
flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement 
is 010. So you need to output 2.

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 
0. So you need to output 0.

'''

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            i = i << 1
        i = i-1
        return i ^ num
        
        '''
        >>>Simple Solution 
        2 to the power index * complement of x
        power = 0 
        comp = 0
        
        while num > 0:
            lsb = num & 1
            num = num >> 1
            x = 0
            if lsb == 0:
                x = 1
            
            comp += pow(2, power)* x
            power += 1
            
        return comp
        '''
        
        
        