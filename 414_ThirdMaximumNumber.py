'''
414. Third Maximum Number

Given a non-empty array of integers, return the third maximum number in this array. If it does 
not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''

import sys

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minNum = -sys.maxint - 1
        fmax = minNum
        smax = minNum
        tmax = minNum
        
        for n in nums:
            if n > fmax:
                tmax = smax
                smax = fmax
                fmax = n
            elif n < fmax and n > smax:
                tmax = smax
                smax = n
            elif n < smax and n > tmax:
                tmax = n
        if tmax != minNum:
            return tmax
        else:
            return max(fmax, smax)
                
                