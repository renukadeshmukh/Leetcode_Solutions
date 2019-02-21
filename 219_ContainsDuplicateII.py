'''
219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two 
distinct indices i and j in the array such that nums[i] = nums[j] and the 
absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

'''
ALGORITM:
1. For every element store the last encountered index and keep checking if 
abs(curr_index - last_encountered) <= k
RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = []
            else:
                abs_diff = abs(i - freq[nums[i]])
                if abs_diff <= k:
                    return True
            freq[nums[i]] = i
        return False
        
        