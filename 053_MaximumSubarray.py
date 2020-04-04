'''
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least 
one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the 
divide and conquer approach, which is more subtle.
'''

'''
ALGORITHM:
Kadane's Algorithm
1. Initialize:
    max_so_far = 0
    max_ending_here = 0
2. Loop for each element of the array
    (a) max_ending_here = max_ending_here + a[i]
    (b) if(max_ending_here < 0)
                max_ending_here = 0
    (c) if(max_so_far < max_ending_here)
                max_so_far = max_ending_here
    return max_so_far

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sm, max_sm = max(nums[0],0), nums[0] 
        for i in range(1, len(nums)):
            cur_sm += nums[i]
            max_sm = max(cur_sm, max_sm)
            
            if cur_sm < 0:
                cur_sm = 0
        return max_sm