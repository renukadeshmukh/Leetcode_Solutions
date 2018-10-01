'''
704. Binary Search

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a 
function to search target in nums. If target exists, then return its index, otherwise return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Note:
You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
'''

'''
ALGORITHM:
Binary Search

RUNTIME COMPLEXITY : O(N)
SPACE COMPLEXITY : O(1)
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarysearch(nums, target, 0, len(nums))
        
    def binarysearch(self, nums, target, startindex, endindex):  
        mid = (startindex + endindex)/2   
        if nums[mid] == target:
            return mid
        elif mid == startindex or mid == endindex:
            return -1
        elif nums[mid] < target:
            return self.binarysearch(nums, target, mid, endindex)
        else:
            return self.binarysearch(nums, target, startindex, mid)
        return -1
s = Solution()
print(s.search([-1,0,3,5,9,12], 9))

print(s.search([-1,0,3,5,9,12], 2))


