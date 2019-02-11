'''
162. Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one 
of the peaks is fine. You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index 
number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak 
element is 2, or index number 5 where the peak element is 6.

Note:
Your solution should be in logarithmic complexity.
'''

'''
ALGORITHM:
1. Scan left to right looking for the peak element. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
Nore:- Can be done in O(LogN) using binary search approach

'''

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        i = 0
        while i < len(nums)-1 and nums[i] < nums[i+1]:
            i += 1
        return i
        