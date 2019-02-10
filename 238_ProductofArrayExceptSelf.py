'''
238. Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that 
output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not 
count as extra space for the purpose of space complexity analysis.)
'''

'''
ALGORITHM:
The product basically is calculated using the numbers before the current number 
and the numbers after the current number. Thus, we can scan the array twice. 
First, we calcuate the running product of the part before the current number. 
Second, we calculate the running product of the part after the current number 
through scanning from the end of the array.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        ln = len(nums)
        p = 1
        for i in range(ln):
            result.append(p)
            p = p * nums[i]
        p = 1 
        for i in range(ln-1,-1,-1):
            result[i] = result[i] * p
            p = p * nums[i]
        return result