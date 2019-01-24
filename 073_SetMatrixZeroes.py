'''
73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. 
Do it in-place.

Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

'''

'''
MY ALGORITHM:
1. Iterate on the matrix.
2. For every cell with value 0, replace the row and column with '#'
3. Iterate over the matrix again, and replace all '#' with 0

RUNTIME COMPLEXITY: (M*N)
SPACE COMPLEXITY: O(M+N) M = no. of rows, N = no. of cols


BETTER ALGORITHM:
1. Use the first cell of every row and column as a flag. This flag would determine 
whether a row or column has been set to zero. This means for every cell instead 
of going to M+NM+N cells and setting it to zero we just set the flag in two cells.

if cell[i][j] == 0 {
    cell[i][0] = 0
    cell[0][j] = 0
}
2. These flags are used later to update the matrix. If the first cell of a row 
is set to zero this means the row should be marked zero. If the first cell of a 
column is set to zero this means the column should be marked zero.
'''
class Solution(object):
    def __init__(self):
        self.visited_row = set()
        self.visited_col = set()
        
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        R,C = len(matrix), len(matrix[0])
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    self.update_row_col(r, c, R, C, matrix)
                    
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == '#':
                    matrix[r][c] = 0
                           
                           
    def update_row_col(self, r, c, R, C, matrix):
        if r not in self.visited_row:
            for j in range(C):
                if matrix[r][j] != 0:
                    matrix[r][j] = '#'
            self.visited_row.add(r)
            
        if c not in self.visited_col:
            for i in range(R):
                if matrix[i][c] != 0:
                    matrix[i][c] = '#' 
            self.visited_col.add(c)