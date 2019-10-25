'''
994. Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten 
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh 
orange.  If this is impossible, return -1 instead. 

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never 
rotten, because rotting only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer 
is just 0.
 
Note:
1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
'''

'''
ALGORITHM:
Breadth-First Search
1. Enque all rotten oranges in a queue
2. Keep dequeing rotten oranges, and mark fresh oranges around this rotten 
   orange as rotten. Enqueue the newly rotten oranges in queue
3. Increment time every time one entire level is processed. 

RUNTIME COMPLEXITY: O(N), where N is number of cells in grid
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sentinel = [-1]
        queue = []
        queue.append(sentinel)
        time, cnt_fresh = 0, 0
        R, C = len(grid), len(grid[0])
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1: cnt_fresh += 1
                elif grid[i][j] == 2: queue.append([i,j])
        
        while len(queue) > 1 and cnt_fresh > 0:
            elem = queue.pop(0)
            if elem[0] == -1:
                time += 1
                queue.append(sentinel)
            else:
                r, c = elem[0], elem[1]
                for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append([nr,nc])
                        cnt_fresh -= 1
        if cnt_fresh == 0:
            return time
        return -1
 

s = Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(s.orangesRotting([[0,2]]))