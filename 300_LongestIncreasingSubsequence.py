'''
300. Longest Increasing Subsequence



'''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = len(nums)
        lis = [1] * ln
        for i in range(ln):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], 1 + lis[j])
        print( lis)

        return max(lis)

s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))