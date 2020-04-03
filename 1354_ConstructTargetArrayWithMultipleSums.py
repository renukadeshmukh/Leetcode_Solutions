'''
1354. Construct Target Array With Multiple Sums
'''

from heapq import heapify

class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        heapify(target, m)
        print(target)

s = Solution()
print(s.isPossible([9,3,5]))
print(s.isPossible([1,1,1,2]))
print(s.isPossible([8,5]))