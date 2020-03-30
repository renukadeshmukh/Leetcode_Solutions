'''
1072. Flip Columns For Maximum Number of Equal Rows

Given a matrix consisting of 0s and 1s, we may choose any number of columns in 
the matrix and flip every cell in that column.  Flipping a cell changes the value 
of that cell from 0 to 1 or from 1 to 0. Return the maximum number of rows that 
have all values equal after some number of flips. 

Example 1:
Input: [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.

Example 2:
Input: [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal 
values.

Example 3:
Input: [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows 
have equal values.
 
Note:
1 <= matrix.length <= 300
1 <= matrix[i].length <= 300
All matrix[i].length's are equal
matrix[i][j] is 0 or 1
'''

'''
ALGORITHM:
1. Convert each row into a tuple and store the number of times the same row
   occues in the given matrix. 
2. Now find the largest value of row + row_complement for this matrix. 

RUNTIME COMPLEXITY: O(M*N) for m rows and n cols. 
SPACE COMPLEXITY: O(M*N)

'''

from collections import defaultdict
class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        max_equal = -1
        
        store = defaultdict(int)
        for row in matrix:
            t = tuple(row)
            store[t] += 1

        for key in store:
            c = store[key]
            t_inv = self.invert(key)
            if t_inv in store:
                c += store[t_inv]
            max_equal = max(max_equal, c)
            
        return max_equal
            
    def invert(self, tup):
        t_inv = []
        for t in tup:
            if t == 0:
                t_inv.append(1)
            else:
                t_inv.append(0)
        return tuple(t_inv)
                    
        