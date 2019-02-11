'''
896. Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A 
is monotone decreasing if for all i <= j, A[i] >= A[j]. Return true if and only 
if the given array A is monotonic.
 

Example 1:
Input: [1,2,2,3]
Output: true

Example 2:
Input: [6,5,4,4]
Output: true

Example 3:
Input: [1,3,2]
Output: false

Example 4:
Input: [1,2,4,5]
Output: true

Example 5:
Input: [1,1,1]
Output: true
 

Note:
1 <= A.length <= 50000
-100000 <= A[i] <= 100000
'''

'''
ALGORITHM:
1. Check for both monotone increasing or monotone decreasing.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return True
        
        mono_inc, mono_dec = True, True
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                mono_inc = False
                break
            
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                mono_dec = False
                break
        
        return mono_inc or mono_dec
            