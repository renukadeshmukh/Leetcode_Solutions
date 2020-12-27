'''
1680. Concatenation of Consecutive Binary Numbers

Given an integer n, return the decimal value of the binary string formed by 
concatenating the binary representations of 1 to n in order, modulo 109 + 7.

 
Example 1:
Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 

Example 2:
Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal 
value 27.

Example 3:
Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.
 
Constraints:
1 <= n <= 105
'''

'''
ALGORITHM:
For num in range 1 to N, the idea is to left shift result by size(number of bits)
in num and then ORinf result and num. For every power of 2, size increases by 1.
To prevent integer overflow, take mod of result after every operation. 

1. For num in range 1 to N:
2.      If num & num-1 = 0, increase size by 1
3.      result = (result << size) | num 
4.      result = result % (1-^9 + 7)
5. return result 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

from collections import deque
from math import pow
class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        modulo = int(pow(10, 9) + 7)
       
        num = 1
        result = 0
        size = 0
        
        while num <= n:
            if (num & (num-1)) == 0:
                size += 1
            result = ((result << size) | num) % modulo
            num += 1
            
        return result
            
        
        
        