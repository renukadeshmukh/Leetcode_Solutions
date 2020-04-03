'''
229. Majority Element II

'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1, num2, count1, count2 = 0,0,0,0
        
        for n in nums:
            if n == num1:
                count1 += 1
            elif n == num2:
                count2 += 1
            elif count1 == 0:
                num1, count1 = n,1
            elif count2 == 0:
                num2, count2 = n,1
            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0,0
        for n in nums:
            if n == num1:
                count1 += 1
            elif n == num2:
                count2 += 1
        
        result = []
        if count1 > len(nums)/3:
            result.append(num1)
        if count2 > len(nums)/3:
            result.append(num2)
        return result
        
            
s = Solution()
print(s.majorityElement([3,2,3]))
print(s.majorityElement([1,1,1,3,3,2,2,2]))

