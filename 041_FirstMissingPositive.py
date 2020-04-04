'''
41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
'''

'''
ALGORITHM:
1. Because we dont care about 0 and negative numbers, replace all instance of x,
   such x < 1 by len(nums) + 1. We now can ignore all numbers > len(nums)
2. Now for every num in nums, if num > 0 and num < len(nums), we negate the index
   at index nums[i], thus marks that nums[i] is present in array and cannot be 
   considered a missing positive. 
3. Repeat for every num in nums. 
4. Now traverse the nums array again and the index of first non-negative num in 
   nums in the answer. 
   
RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: (1)
'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = len(nums)
        for i in range(len(nums)):
            if nums[i] < 1:
            nums[i] = ln+1
        
        for i in range(ln):
            n = abs(nums[i])
            if n > 0 and n <= ln:
                if nums[n-1] > 0:
                    nums[n-1] *= -1
    
        i = 0
        while i < ln:
            if nums[i] >= 0:
                break
            i += 1
        return i+1