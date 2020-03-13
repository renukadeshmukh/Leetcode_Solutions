'''
628. Maximum Product of Three Numbers

Given an integer array, find three numbers whose product is maximum and output 
the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
 
Example 2:
Input: [1,2,3,4]
Output: 24
 
Note:
The length of the given array will be in range [3,104] and all elements are in 
the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 
32-bit signed integer.
'''

'''
ALGORITHM:
1. We need to only find the required 2 smallest values(min1 and min2) and the 
   three largest values(max1, max2, max3) in the nums array, by iterating over 
   the nums array only once.
2. At the end, again we can find out the larger value out of min1 * min2 * max1
   and max1 * max2 * max3 to find the required maximum product.
   
RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        min1 = max1 = nums[0]
        min2, max2 ,max3 = None, None, None
        for i in range(1, len(nums)):
            num = nums[i]
            if num <= min1:
                min1, min2 = num, min1,
            elif min2 == None or num <= min2:
                min2 = num
            
            if num >= max1:
                max1, max2, max3 = num, max1, max2
            elif max2 == None or num >= max2:
                max2, max3 = num, max2
            elif max3 == None or num > max3:
                max3 = num
                
        return max(min1 * min2 * max1, max1 * max2 * max3) 

s = Solution()
print(s.maximumProduct([-1, -2, -3]))
print(s.maximumProduct([1,2,3]))
print(s.maximumProduct([1,2,3, 4]))
