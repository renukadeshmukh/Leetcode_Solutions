'''
665. Non-decreasing Array

'''

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in xrange(1, len(nums)):
            if count == 2:
                break
            elif nums[i-1] > nums[i]:
                nums[i] = nums[i-1]
                count += 1
        if count == 2:
            return False
        return True
            
        
s = Solution()
print(s.checkPossibility([3,4,2,3]))

s = Solution()
print(s.checkPossibility([4,2,3]))

s = Solution()
print(s.checkPossibility([4,2,1]))