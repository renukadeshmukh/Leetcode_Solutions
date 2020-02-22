'''
1162. As Far from Land as Possible

Given an N x N grid containing only values 0 and 1, where 0 represents water and 
1 represents land, find a water cell such that its distance to the nearest land 
cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance 
between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

Example 1:
Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:
Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.
 
Note:
1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1
'''

'''
ALGORITHM: 
Breadth First Search. (The last zero found is the farthest for all lands.)
1. Iterate over the grid and enqueue all land co-ordinates. 
2. Keep dequeuing each co-ordinates from queue and enqueue surrounding valid
   cells if the cell has water. Mark the cell as visited. 
3. Repeat till no more water is left unvisited. 
4. The last water cell to be encountered is farthest for land.
5. Keep track of number distance using a sentinel.
6. Return the max distance. 

RUNTIME COMPLEXITY: O(N*N)
SPACE COMPLEXITY: O(N*N) for stack space
'''

from collections import deque
class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        q.append(['#'])
        cnt_land, cnt_water = 0, 0
        N = len(grid)

        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    q.append([i,j])
                    cnt_land += 1
                else:
                    cnt_water += 1
        
        if cnt_water==0 or cnt_land==0:
            return -1

        dist = -1
        while len(q) > 1:
            arr = q.popleft()
            if arr[0] == '#':
                dist += 1
                q.append(['#'])
            else:
                i, j = arr[0], arr[1]
                if  i > 0  and grid[i-1][j] == 0:
                    q.append([i-1, j])
                    grid[i-1][j] = 1
                if i < N-1 and grid[i+1][j] == 0:
                    q.append([i+1, j])
                    grid[i+1][j] = 1
                if j > 0 and grid[i][j-1] == 0:
                    q.append([i, j-1])
                    grid[i][j-1] = 1
                if j < N-1 and grid[i][j+1] == 0:
                    q.append([i, j+1])
                    grid[i][j+1] = 1
        return dist


s = Solution()
print(s.maxDistance([[1,0,1],[0,0,0],[1,0,1]]))
print(s.maxDistance([[1,0,0],[0,0,0],[0,0,0]]))
               