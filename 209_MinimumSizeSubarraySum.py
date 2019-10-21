'''
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal 
length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 
0 instead.

Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which 
the time complexity is O(n log n). 
'''

'''
ALGORITHM:
1. Maintain 2 pointers i and j. i is incremented for every iteration. j is 
   incremented only when cur_sum >= target_sum.
   i = 0 and j = 0
2. While cur_sum < target_sum, keep incremnting i and adding nums[i] to cur_sum
3. Once cur_sum >= target_sum, update min_len_subarry as (i - j + 1)
3. Keep incremnting j will j < i and cur_sum >= target. Also keep updating 
   min_len_subarry to keep track of minimum subarray. 
4. Return min_len_subarry

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''
from sys import maxsize
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 0
        s1 = 0
        min_subarr_len = maxsize
        while i < len(nums):
            s1 += nums[i]
            if s1 >= s:
                min_subarr_len = min(min_subarr_len, i-j+1)
                while j < i and s1 >= s:
                    s1 -= nums[j]
                    j += 1
                    if s1 >= s:
                        min_subarr_len = min(min_subarr_len, i-j+1)

            #else:
            #    s1 += nums[i]
            i += 1
        return min_subarr_len

s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))