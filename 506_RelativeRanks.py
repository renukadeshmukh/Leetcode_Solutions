'''
506. Relative Ranks

Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]


'''

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        dct = {}
        i = 0
        for n in nums:
            dct[n] = i
            i+=1 
        nums.sort(reverse=True)
        result = [''] * len(nums)
        
        for i in range(len(nums)):
            n = nums[i]
            val = dct[n]
            if i in [0,1,2]:
                if i == 0:
                    result[val] = "Gold Medal"
                if i == 1:
                    result[val] = "Silver Medal"
                if i == 2:
                    result[val] = "Bronze Medal"
            else:
                result[val] = str(i+1)
        return result 
                
        
        