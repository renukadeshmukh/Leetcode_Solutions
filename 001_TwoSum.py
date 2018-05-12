'''
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tsdict = {}
        i=0
        for n in nums:
            if not tsdict.has_key(n) :
                tsdict[n] = []
            tsdict[n].append(i)
            i += 1
            
        i=0;
        j=len(nums) - 1
        nums.sort()
        while True:
            sum = nums[i] + nums[j]
            if sum == target:
                break
            elif sum < target:
                i += 1
            else:
                j -= 1

        if nums[i] != nums[j]:
            return [tsdict[nums[i]][0], tsdict[nums[j]][0]]
        else:
            return [tsdict[nums[i]][0], tsdict[nums[j]][1]]
s = Solution()
print s.twoSum([0,4,3,0] , 0)