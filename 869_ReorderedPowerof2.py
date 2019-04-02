'''
869. Reordered Power of 2

Starting with a positive integer N, we reorder the digits in any order 
(including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting 
number is a power of 2. 

Example 1:
Input: 1
Output: true

Example 2:
Input: 10
Output: false

Example 3:
Input: 16
Output: true

Example 4:
Input: 24
Output: false

Example 5:
Input: 46
Output: true
 
Note:
1 <= N <= 10^9
'''

'''
ALGORITHM:
1. We can check whether two numbers have the same digits by comparing the count 
of their digits. For example, 338 and 833 have the same digits because they both 
have exactly two 3's and one 8.

Since NN could only be a power of 2 with 9 digits or less (namely, 2^0, 2^1...2^29), 
we can just check whether N has the same digits as any of these possibilities

RUNTIME COMPLEXITY: O(logN * logN) . There are logN different candidate powers 
of 2, and each comparison has O(logN) time complexity
SPACE COMPLEXITY: O(logN)
'''

class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        c = collections.Counter(str(N))
        for i in range(30):
            p = str(1 << i)
            if collections.Counter(p) == c:
                return True
        return False

