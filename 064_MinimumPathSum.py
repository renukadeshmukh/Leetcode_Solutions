'''
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left 
to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

'''
ALGORITHM:
1. We can calculate the minimum path length to each entry of the grid. 
2. Because the problem only allows for right and downward movements, we only 
   need to compare two possible paths to each element(from the top or the left). 
   The answer is the value at the bottom right. We don't need extra space 
   because we will never need to reuse any values.

RUNTIME COMPLEXITY: O(M*N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])

        for i in range(1, len(grid[0])):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        for i in range(1, len(grid)):
            grid[i][0] = grid[i-1][0] + grid[i][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
            
        return grid[M-1][N-1]