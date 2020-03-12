'''
1260. Shift 2D Grid

Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
In one shift operation:
Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Example 1:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2:
Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]

Constraints:
m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
'''

'''
ALGORITHM:
1. Traverse the array, and store elements in an adhoc array called store. 
2. Starting from  i = (len(store) - k)%len(store), copy the elements back to the 
   grid. 

RUNTIME COMPLEXITY: O(M*N)
SPACE COMPLEXITY: O(M*N)
'''

class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        if not grid:
            return grid
        m, n = len(grid), len(grid[0])
        ln = m*n
        store = []
        
        for i in range(m):
            for j in range(n):
                store.append(grid[i][j])
        
        k = ln - k
        for i in range(m):
            for j in range(n):
                k = k % ln 
                grid[i][j] = store[k]
                k += 1
        return grid
        
                