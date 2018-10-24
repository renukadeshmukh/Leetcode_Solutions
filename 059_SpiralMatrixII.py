'''
59. Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1
to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

'''
ALGORITHM:
1. Initialize rowStart, rowEnd, colStart and colEnd
2. Fill up the first row, by incrementing j and i = rowStart, then rowStart += 1
3. Fill up the last column by incrementing i and j = colEnd, then colEnd -= 1
4. Fill up last row by decrementing j and i = rowEnd, then rowEnd -= 1
5. Fill up the first column by decrementing i and j = colStart, then colStart += 1
6. Repeat steps 2 through 5 till rowStart <= rowEnd and colStart <= colEnd

RUNTIME COMPLEXITY: O(N^2)
SPACE COMPLEXITY: O(N^2)

'''

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = self.initialize(n)
        rowStart, rowEnd, colStart, colEnd = 0, n-1, 0, n-1
        num = 1

        while rowStart <= rowEnd and colStart <= colEnd:
            for j in range(colStart, colEnd+1):
                res[rowStart][j] = num
                num += 1
            rowStart += 1

            for i in range(rowStart, rowEnd+1):
                res[i][colEnd] = num
                num += 1
            colEnd -= 1

            for j in range(colEnd, colStart-1, -1):
                res[rowEnd][j] = num
                num += 1
            rowEnd -= 1

            for i in range(rowEnd, rowStart-1, -1):
                res[i][colStart] = num
                num += 1
            colStart += 1
        
        return res
    
    def initialize(self, n):
        res = []
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(0)
            res.append(tmp)
        return res

s = Solution()
s.generateMatrix(3)           
        