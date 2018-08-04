'''
661. Image Smoother

Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to 
make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding 
cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].

'''

'''
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
'''

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        m, n = len(M), len(M[0])
        for i in range(m):
            row = []
            for j in range(n):
                row.append(self.get_gray_scale(M, i, j, m ,n))
            res.append(row)
        return res    
    
    def get_gray_scale(self, M, i, j, m, n):
        corner1, corner2, corner3, corner4, up, down, left, right = 0,0,0,0,0,0,0,0
        div = 1
        print(i,j)
        
        if i > 0:
            up, div = M[i-1][j], div+1
        if i < m-1:
            down,div = M[i+1][j], div+1
        if j > 0:
            left,div = M[i][j-1],div+1
        if j < n-1:
            right,div = M[i][j+1],div+1
           
        if i > 0 and j>0:
            corner1,div = M[i-1][j-1], div+1
        if i< m-1 and j>0:
            corner2,div = M[i+1][j-1],div+1
        if i <m-1 and j<n-1:
            corner3,div = M[i+1][j+1],div+1
        if i>0 and j<n-1:
            corner4, div = M[i-1][j+1], div+1

        gray_scale = (M[i][j] + corner1 + corner2 + corner3 + corner4 + left + right + up + down) // div
        return gray_scale

s = Solution()
input = [[1,1,1], [1,0,1], [1,1,1]]
result = s.imageSmoother(input)
print(result)