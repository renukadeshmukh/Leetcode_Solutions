'''

198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of 
money you can rob tonight without alerting the police.

'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len1 = len(nums) - 1
        if len1 == -1:
            return 0
        elif len1 == 0:
            return nums[len1]
        else:
            memo = []
            i = 0
            while i <= len1:
                memo.append( -1)
                i += 1
            return max(self.getmax(nums, 0, len1, memo), self.getmax(nums[1:], 0, len1-1, memo[1:]))
            
    def getmax(self, nums, indx, len1, memo):
        
        if indx == len1:
            memo[indx] = nums[indx]
            return nums[indx]
        elif indx == len1-1:
            memo[indx] = max(nums[indx], nums[indx+1])
            return memo[indx]
        elif indx == len1-2:
            memo[indx] = max(nums[indx] + nums[indx+2], nums[indx+1])
            return memo[indx]
        else:
            if memo[indx+2] == -1:
                memo[indx+2] = self.getmax(nums, indx+2, len1, memo)
            if memo[indx+3] == -1:
                memo[indx+3] = self.getmax(nums, indx+3, len1, memo)
                
            return nums[indx] + max(memo[indx+2], memo[indx+3])
        
        
