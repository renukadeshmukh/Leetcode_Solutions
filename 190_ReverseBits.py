'''
190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

Example:
Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
Follow up:
If this function is called many times, how would you optimize it?
'''

from math import pow
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        i=0
        while i < 32:
            right_bit = n & 1
            n = n >> 1
            result = result << 1
            result = result | right_bit
            i +=1
        return result

s = Solution()
res = s.reverseBits(43261596)
print(res)