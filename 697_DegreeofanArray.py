'''
697. Degree of an Array

Given a non-empty array of non-negative integers nums, the degree of this array 
is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of 
nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
'''

'''
ALGORITHM:
1. Iterate over the array and store index of each element in a dict
2. Iterate over the dict and find the difference of first and last index of each
   element to find the size of subarray with highest degree. 
RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        for i in range(len(nums)):
            if nums[i] not in num_dict:
                num_dict[nums[i]] = []
            num_dict[nums[i]].append(i)
        
        mx_len = 1
        min_subarr_len = 50001
        for key in num_dict:
            ln = len(num_dict[key])
            if ln > 1:
                if ln == mx_len:
                    sub_arr_ln =  num_dict[key][-1] - num_dict[key][0] + 1
                    min_subarr_len = min(min_subarr_len, sub_arr_ln)
                elif ln > mx_len:
                    mx_len = ln
                    min_subarr_len = num_dict[key][-1] - num_dict[key][0] + 1 
        if min_subarr_len == 50001:
            return 1   
        return min_subarr_len
                
s = Solution()
print(s.findShortestSubArray([1, 2, 2, 3, 1])) #2
print(s.findShortestSubArray([1,2,2,3,1,4,2])) #6