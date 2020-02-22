'''
1091. Shortest Path in Binary Matrix

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is 
composed of cells C_1, C_2, ..., C_k such that:
Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are 
different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).

Return the length of the shortest such clear path from top-left to bottom-right.  
If such a path does not exist, return -1.

Example 1:
Input: [[0,1],[1,0]]
Output: 2

Example 2:
Input: [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Note:
1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1
'''

'''
ALGORITHM:
1. Use BFS to find the shortest path 
2. Start from grid[0][0] and enqueue all connected 0-cells (8 way)
3. Dequeue a cell from queue and enqueue connected unvisited 0-cells. 
   Continue this operation till no more connected 0 left or you have reached 
   grid[N-1][N-1]
4. Keep track of length of path using a sentinel. 

RUNTIME COMPLEXITY: O(N*N)
SPACE COMPLEXITY: O(N*N) for queue
'''

from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        if not grid or grid[0][0] != 0 or grid[N-1][N-1] != 0:
            return -1
        
        q = deque()
        q.append([0,0])
        q.append(['#'])
        result = 1
        combinations = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        while len(q) > 1:
            elem = q.popleft()
            if elem[0] == '#':
                result += 1
                q.append(['#'])
            else:
                r, c = elem[0], elem[1]
                if r == N-1 and c == N-1:
                    break
                else:
                    for cbn in combinations:
                        nr, nc = r + cbn[0], c + cbn[1]
                        if 0<= nr< N and 0<= nc< N and grid[nr][nc] == 0:
                            q.append([nr,nc])
                            grid[nr][nc] = 1
        if r == N-1 and c == N-1:
            return result
        return -1
     
    
s = Solution()
print(s.shortestPathBinaryMatrix([[0,1],[1,0]]))
print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,1]]))