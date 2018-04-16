'''
766. Toeplitz Matrix

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:
---------
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: True
Explanation:
1234
5123
9512
In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", and 
in each diagonal all elements are the same, so the answer is True.

Example 2:
---------
Input: matrix = [[1,2],[2,2]]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:
-----
matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

'''

class Solution(object):
    '''
    Solution : Check if each diagonal is a Toeplitz Diagonal, i.e. check if each diagonal has the same integers. 
    '''
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        res = s.checkToeplitzDiagonal(0, 0, m, n, matrix)
        
        if not res:
            return False
        for i in range(1,m):
            res = self.checkToeplitzDiagonal(i, 0, m, n, matrix)
            if not res:
                break
        if not res:
            return False
        for i in range(1,n):
            res = self.checkToeplitzDiagonal(0, i, m, n, matrix)
            if not res:
                break
        
        return res
            
    def checkToeplitzDiagonal(self, row, col, m , n, matrix):
        val = matrix[row][col]
        i, j = (row+1, col+1)
        res = True
        while i < m and j < n:
            if matrix[i][j] != val:
                res = False
                break
            i += 1
            j += 1
        return res
        
s = Solution()
mat_input = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
res = s.isToeplitzMatrix(mat_input)
print(res)