'''
868. Binary Gap

Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary 
representation of N.

If there aren't two consecutive 1's, return 0.

Example 1:

Input: 22
Output: 2
Explanation: 
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.
Example 2:

Input: 5
Output: 2
Explanation: 
5 in binary is 0b101.
Example 3:

Input: 6
Output: 1
Explanation: 
6 in binary is 0b110.
Example 4:

Input: 8
Output: 0
Explanation: 
8 in binary is 0b1000.
There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.
 

Note:

1 <= N <= 10^9

'''

'''
ALGORITHM:
1. Get binary represeantation b of N
2. Iterate on b and keep track of distance between 1's
3. return max distance

TIME COMPLEXITY: O(1) as binary representation of a number can be max 32 bit
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        b = bin(N)
        dist = 0
        last_1 = -1
        for i in range(2, len(b)):
            if b[i] == '1':
                if last_1 == -1:
                    last_1 = i
                else:
                    dist = max(dist, i-last_1)
                    last_1 = i
        return dist

print(Solution().binaryGap(22))
print(Solution().binaryGap(5))
print(Solution().binaryGap(6))
print(Solution().binaryGap(8))
        