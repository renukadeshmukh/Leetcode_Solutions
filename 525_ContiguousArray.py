'''
525. Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with 
equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: 
[0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: 
[0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
'''

'''
ALGORITHM:
1. Maintain a count variable, which is used to store the relative number of 1s 
   and 0s encountered so far while traversing the array. The count variable is 
   incremented by one for every 1 and the same is decremented by one for every 0 
   encountered.
2. We start traversing the array from the beginning. If at any moment, the count 
   becomes zero, it implies that we've encountered equal number of zeros and 
   ones from the beginning till the current index of the array[i]. Not only this, 
   another point to be noted is that if we encounter the same count twice while 
   traversing the array, it means that the number of zeros and ones are equal 
   between the indices corresponding to the equal countcount values. 
3. Use a HashMap to store the entries in the form of (count, index). We make an 
   entry for a count in the map whenever the count is encountered first, and 
   later on use the correspoding index to find the length of the largest 
   subarray with equal no. of 0s and 1s when the same count is encountered again.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_map = {}
        count_map[0] = -1
        max_ln, cur_count = 0, 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                cur_count -= 1
            else:
                cur_count += 1
            
            if cur_count in count_map:
                max_ln = max(max_ln, i - count_map[cur_count])
            else:
                count_map[cur_count] = i
        
        return max_ln
                