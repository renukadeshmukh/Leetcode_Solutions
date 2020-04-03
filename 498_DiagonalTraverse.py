'''
498. Diagonal Traverse
'''

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        dir_up = True
        i, j, n, m = 0, 0, len(matrix), len(matrix[0])
        result = []
        
        while i < n and j < m:
            result.append(matrix[i][j])
            
    
    
    def is_valid_col(self, j, m):
        return j >= 0 and j < m

    def is_valid_row(self, i, n):
        return i >= 0 and i < n 

s = Solution()
result = s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
print(result)