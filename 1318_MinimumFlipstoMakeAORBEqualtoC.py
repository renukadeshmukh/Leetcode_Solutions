'''
1318. Minimum Flips to Make a OR b Equal to c

Given 3 positives numbers a, b and c. Return the minimum flips required in some 
bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 
in their binary representation.

Example 1:
Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

Example 2:
Input: a = 4, b = 2, c = 7
Output: 1

Example 3:
Input: a = 1, b = 2, c = 3
Output: 0

Constraints:
1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9
'''

'''
ALGORITHM: 
1. Keep extracting the LSB(Least significant bit) for a, b and c and calculate 
   the number of bit to be modified and update answer. 
2. Right-shift a,b and c

Comparison rules:
1. If lsb_a | lsb_b = 0 but lsb_c = 1, inc answer by 1 as we need to either make
   lsb_a or lsb_b equal to 1
2. If  lsb_a | lsb_b = 1 but lsb_c = 0, then make all 1 bits to 0 and inc answer
   for every operation (inc by 2 if both lsb_a and lsb_b are 1, else inc by 1)

RUNTIME COMPLEXITY: O(32) = O(1)
SPACE COMPLEXITY = O(1)
'''

class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        a_or_b = a | b
        answer = 0
        
        while a > 0 or b > 0 or c > 0:
            lsb1, lsb2, lsb3 = a&1, b&1, c&1
            
            if lsb3 == 1 and lsb1 | lsb2 == 0 :
                answer += 1
            elif lsb3 == 0:
                if lsb1 == 1:
                    answer += 1
                if lsb2 == 1:
                    answer += 1
            a, b, c = a>>1, b>>1, c>>1
        return answer