'''
845. Longest Mountain in Array
'''

class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ln = len(A)
        max_mt = 0
        end = 0
        
        while end < ln:
            start = end
            while end < ln-1 and A[end] < A[end+1]:
                end += 1
            while end < ln-1 and A[end] > A[end+1]:
                end += 1
            max_mt = max(max_mt , end-start+1)
            end += 1
            
        return max_mt
            
        
s = Solution()
print(s.longestMountain([2,2,2]))
print(s.longestMountain([2,1,4,7,3,2,5]))