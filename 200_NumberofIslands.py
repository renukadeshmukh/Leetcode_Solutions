'''
200. Number of Islands

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
2. If cell == 1, increase island count by 1
3. Recursively mark all connected cells with value 1 as visited. 
4. Return count. 

RUNTIME COMPLEXITY: O(row * col)
SPACE COMPLEXITY: O(row * col) for stack space
'''


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if  grid[row][col] == "1":
                    self.mark_island(grid, row, col)
                    count += 1
        return count
                    
                    
    def mark_island(self, grid, i, j):
        grid[i][j] = "v"
        if i > 0 and grid[i-1][j] == "1":
            self.mark_island(grid, i-1, j )
        if j > 0 and grid[i][j-1] == "1":
            self.mark_island(grid, i, j-1 )
        if i < len(grid)-1 and grid[i+1][j] == "1":
            self.mark_island(grid, i+1, j )
        if j < len(grid[0])-1 and grid[i][j+1] == "1":
            self.mark_island(grid, i, j+1 )
 

s = Solution()
print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
print(s.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))