'''
910. Smallest Range II
'''

class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        max_a = -1
        min_a = 10001
        
        avg = sum(A)/len(A)
        print(avg)
        
        for a in A:
            a_new  = 0
            if a < avg:
                a_new = a + K
            else:
                a_new = a - K
                
            min_a = min(min_a, a_new)
            max_a = max(max_a, a_new)
        return max_a - min_a

s = Solution()
print(s.smallestRangeII([1], 0))
print(s.smallestRangeII([0,10], 2))
print(s.smallestRangeII([1,3,6], 3))