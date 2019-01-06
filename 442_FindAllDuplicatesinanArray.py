'''
442. Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements 
appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[2,3]
'''

'''
ALGORITHM:
1. For every element n in the array, negate the index e.
2. if index e is already negative, it means e is a duplicate number.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for n in nums:
            i = abs(n)-1
            if nums[i] < 0:
                res.append(abs(n))
            else:
                nums[i] = nums[i] * -1
        return res
