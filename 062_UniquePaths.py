'''
62. Unique Paths

A robot is located at the top-left corner of a m x n grid.
The robot can only move either down or right at any point in time. The robot is 
trying to reach the bottom-right corner of the grid.
How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right 
corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28
'''

'''
ALGORITHM:
1. If there is just one row or column, there is only one way to get from START
   to FINISH.
2. As the robot can only move right and down, to get from start to finish, for 
   every grid, we should calculate the number of ways to get to grid[i][j]. 
3. As you can get to grid[i][j] from top and left, the number of ways to get to 
   grid[i][j] = grid[i-1][j] + grid[i][j-1]
4. Fill in the values for the M*N grid
5. Return grid[n-1][m-1] as final answer.

RUNTIME COMPLEXITY: O(M*N)
SPACE COMPLEXITY: O(M*N)
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        store =  [[0 for i in xrange(m)] for j in xrange(n)]
        
        for i in range(n):
            store[i][0] = 1
        for i in range(m):
            store[0][i] = 1
          
        for i in range(1, n):
            for j in range(1, m):
                store[i][j] = store[i-1][j] + store[i][j-1]
        
        return store[n-1][m-1]