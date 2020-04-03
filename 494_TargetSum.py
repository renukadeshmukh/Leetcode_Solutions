'''
494. Target Sum
'''

class Solution(object):

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self.findTargetSumWaysHelper(nums, 0, 0, S, '')
    
    def findTargetSumWaysHelper(self, nums, i, current, target, s):
        if i == len(nums) and current == target:
            print(s)
            return 1
        elif i == len(nums) and current != target:
            print(s)
            return 0
        else:
            r1 = self.findTargetSumWaysHelper(nums, i+1, current + nums[i], target, s + '+' + str(nums[i])) 
            r2 = self.findTargetSumWaysHelper(nums, i+1, current - nums[i], target, s + '-' + str(nums[i]))
            return r1 + r2
            
        
s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))