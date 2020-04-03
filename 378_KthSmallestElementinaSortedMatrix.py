

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        i,j,n = (0,0, len(matrix))
        _sorted = [matrix[i][j]]
        while i < n and j < n:
            i1, j1, i2, j2 = (i, j, i, j + 1)
            
            
        
            
    def merge(self, l1, l2):
        _sorted = []
        i, j = (0,0)
        
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                _sorted.append(l1[i])
                i += 1
            else:
                _sorted.append(l2[j])
                j += 1
        _sorted.extend(l1[i:])
        _sorted.extend(l2[j:])
        return _sorted
        
s = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
] 
print(s.kthSmallest(matrix, 8))