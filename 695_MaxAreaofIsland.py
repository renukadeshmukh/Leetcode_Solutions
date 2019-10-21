'''
695. Max Area of Island

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands 
horizontally or vertically. You may assume all four edges of the grid are all 
surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
'''

'''
ALGORITHM:
1. Iterate over the matrix.
2. If cell == 1, Recursively calculate size of this island by checking top, left,
   right and bottom cells. Marks all visited cells with -1 so as not to 
   consider them again.  
3. Keep track of max area seen and return max_area 

RUNTIME COMPLEXITY: O(row * col)
SPACE COMPLEXITY: O(row * col) for stack space
'''

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if  grid[row][col] == 1:
                    area = self.calculate_area(grid, row, col, 0)
                    max_area = max(max_area, area)
        return max_area
                    
                    
    def calculate_area(self, grid, i, j, area):
        grid[i][j] = -1
        #area += 1
        right, left, top, bottom = 0, 0, 0,0
        if i > 0 and grid[i-1][j] == 1:
            top = self.calculate_area(grid, i-1, j, area )
        if j > 0 and grid[i][j-1] == 1:
            left = self.calculate_area(grid, i, j-1, area )
        if i < len(grid)-1 and grid[i+1][j] == 1:
            bottom =  self.calculate_area(grid, i+1, j, area )
        if j < len(grid[0])-1 and grid[i][j+1] == 1:
            right = self.calculate_area(grid, i, j+1, area )
        #print(area)
        return 1 + left + right + top + bottom
        
s = Solution()
#print(s.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
print(s.maxAreaOfIsland([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))