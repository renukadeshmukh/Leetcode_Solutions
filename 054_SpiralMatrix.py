'''
54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the 
matrix in spiral order.

Example 1
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

'''
ALGORITHM:
1. Initialize rowStart, rowEnd, colStart and colEnd
2. Get the first row, by incrementing j and i = rowStart, then rowStart += 1
3. Get the last column by incrementing i and j = colEnd, then colEnd -= 1
4. Get last row by decrementing j and i = rowEnd, then rowEnd -= 1
5. Get the first column by decrementing i and j = colStart, then colStart += 1
6. Repeat steps 2 through 5 till rowStart <= rowEnd and colStart <= colEnd

RUNTIME COMPLEXITY: O(N^2)
SPACE COMPLEXITY: O(N^2)

'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rowStart, rowEnd, colStart, colEnd = 0, len(matrix) -1, 0, len(matrix[0]) - 1
        res = []
        if matrix == []:
            return []
        while rowStart <= rowEnd and colStart <= colEnd:
            for j in range(colStart, colEnd+1):
                res.append(matrix[rowStart][j])
            rowStart += 1

            for i in range(rowStart, rowEnd+1):
                res.append(matrix[i][colEnd])
            colEnd -= 1

            if rowStart <= rowEnd:
                for j in range(colEnd, colStart-1, -1):
                    res.append(matrix[rowEnd][j])
                rowEnd -= 1

            if colStart <= colEnd:
                for i in range(rowEnd, rowStart-1, -1):
                    res.append(matrix[i][colStart])
                colStart += 1
        
        return res

s = Solution()
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

#[1,2,3,4,8,12,11,10,9,5,6,7]