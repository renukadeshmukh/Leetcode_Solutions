'''
303. Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices i and 
j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''

'''
ALGORITHM:
1. For rach num in array, save sum of index 0 to i in a new array
2. For sum of index i to j, sum_till_j - sum_till_i

RUNTIME COMPLEXITY: 
  __init__ : O(N)
  sumRange : O(1)
SPACE COMPLEXITY:
  __init__ : O(N)
  sumRange : O(1)
'''
class NumArray(object):
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.num_arr = [0]
        for num in nums:
            self.num_arr.append(self.num_arr[-1] + num)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return (self.num_arr[j+1] - self.num_arr[i])
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
