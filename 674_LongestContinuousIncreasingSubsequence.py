'''
674. Longest Continuous Increasing Subsequence

Given an unsorted array of integers, find the length of longest continuous 
increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length 
is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous 
one where 5 and 7 are separated by 4. 

Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
Note: Length of the array will not exceed 10,000.
'''

'''
ALGORITHM:
1. For num in nums:
    if next_num > cur_num => inc cur_len
    else max_len = max(cur_len, max_len)
2. return max_len

RUNTIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_ln,cur_ln,ln = 0, 1, len(nums) - 1
        
        i = 0
        while i < ln:
            if nums[i] < nums[i+1]:
                cur_ln += 1
            else:
                max_ln = max(max_ln, cur_ln)
                cur_ln = 1
            i += 1
        max_ln = max(max_ln, cur_ln)
        return max_ln