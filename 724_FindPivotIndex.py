'''
724. Find Pivot Index

Given an array of integers nums, write a method that returns the "pivot" index 
of this array. We define the pivot index as the index where the sum of the numbers 
to the left of the index is equal to the sum of the numbers to the right of the 
index. If no such index exists, we should return -1. If there are multiple pivot 
indexes, you should return the left-most pivot index.

Example 1:
Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum 
of numbers to the right of index 3. Also, 3 is the first index where this occurs.
 

Example 2:
Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.

Note:
The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].
'''

'''
ALGORITHM:
1. Sum all element from left to right. (right) 
2. Maintain sum of elements on right and elements on left. 
3. If right == left, return index, else return -1.
 
RUNTIME COMPLEXITY: (N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = sum(nums)
        
        for index, num in enumerate(nums):
            right-=num
            if left==right:
                return index
            left+=num
        return -1