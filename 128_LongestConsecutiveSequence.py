'''
128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive 
elements sequence.
Your algorithm should run in O(n) complexity.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
Therefore its length is 4.

'''

'''
ALGORITHM:
1. Convert nums to a set 'all_nums', initialize a set 'visited' as empty
2. For every number n in all_nums, if n-1 present in all_nums, skip the number
   for now. This number will be considered later
3. Else, while you keep finding n+1 in all_nums, inc cur_streak_length and 
   adding n+1 to visited, so they are not considered again.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_nums = set(nums)
        visited = set()
        max_streak = 0
        for n in nums:
            if n-1 in all_nums:
                continue
            if n not in visited:
                visited.add(n)
                cur_streak_length = 1
                x = n
                while x+1 in all_nums:
                    visited.add(n+1)
                    cur_streak_length += 1
                    x += 1
                max_streak = max(max_streak, cur_streak_length)
        return max_streak
            
        
        
