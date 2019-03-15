'''
55. Jump Game

Given an array of non-negative integers, you are initially positioned at the 
first index of the array. Each element in the array represents your maximum jump 
length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
            jump length is 0, which makes it impossible to reach the last index.
'''

'''
ALGORITHM:
1. Maintain a cumulative - max distance you can go from current node. 
2. If cumulative > length of nums, retrun True
3. If cumulative = 0, but you havnt reached the end, return False

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        ln = len(nums)
        if len(nums) <= 1:
            return True
        cumulative = 1
        for i in range(ln):
            cumulative = max(nums[i], cumulative-1)
            if cumulative <= 0 and i != ln-1:
                return False
            elif cumulative >= ln-1:
                return True
        return True


s = Solution()
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))
print(s.canJump([0]))
print(s.canJump([0,1]))