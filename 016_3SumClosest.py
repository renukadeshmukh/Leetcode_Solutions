'''
16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that 
the sum is closest to target. Return the sum of the three integers. You may assume that each 
input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_diff = sys.maxint
        nums.sort()
        res = sys.maxint
        leng = len(nums) - 2
        for i in range(leng):
            j = i+1
            k = leng + 1
            found = False
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                else:
                    diff = abs(target - s)
                    if diff <= min_diff:
                        min_diff = diff
                        res = s
                    if s > target:
                        k -=1
                    else:
                        j += 1
                        
            i += 1
        return res
        
 