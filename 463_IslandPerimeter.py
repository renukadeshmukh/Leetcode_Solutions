'''
463. Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16

'''

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += self.getPerimeterForCell(grid, i, j, m, n)
        return perimeter
                    
                        
                        
                        
    def getPerimeterForCell(self, grid, i, j, m, n):
        pm = 4
        if j>0 and grid[i][j-1] == 1:
            pm -=1
        if j < n-1 and grid[i][j+1] == 1:
            pm -=1
        if i > 0  and grid[i-1][j] == 1:
            pm -=1
        if i < m-1 and grid[i+1][j] == 1:
            pm -=1
        return pm
