'''
46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = self.permute_helper(nums, [], [])
        print res
        
    def permute_helper(self, nums, res, temp):
        if len(nums) == 0: 
            print(temp)
            res.append(temp)
            temp = []
        
        for i in range(len(nums)):
            temp.append(nums[i])
            print nums
            nums = nums[0 : i] + nums[i+1 : ]
            self.permute_helper(nums, res, temp)
        return res
            
s = Solution()
arr = [1,2,3]
print s.permute(arr)