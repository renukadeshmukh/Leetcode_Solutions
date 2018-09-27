'''
228. Summary Ranges

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
'''

'''
ALGORITHM:
1. Iterate on the array, 
2. if nums[i+1] != nums[i] + 1, output the range

RUNTIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
'''
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        first_flag = True
        res = []
        s = ''
        ln = len(nums)-1
        for i in xrange(ln):
            if first_flag:
                if nums[i+1] != nums[i] + 1:
                    res.append(str(nums[i]))
                else:
                    s += str(nums[i]) + '->'
                    first_flag = False
            elif nums[i+1] != nums[i] + 1:
                s += str(nums[i])
                res.append(s)
                s = ''
                first_flag = True
        s += str(nums[-1])
        res.append(s)
        return res

s = Solution()
print(s.summaryRanges([0,2,3,4,6,8,9]))
#["0","2->4","6","8->9"]

print(s.summaryRanges([0,1,2,4,5,7]))
#["0->2","4->5","7"]