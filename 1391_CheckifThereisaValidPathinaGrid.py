'''
1391. Check if There is a Valid Path in a Grid
'''

from collections import deque
class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        directions = {1: [(0, -1), (0, 1)], 
                      2: [(-1, 0), (1, 0)],
                      3: [(0, -1), (1, 0)],
                      4: [(0, 1), (1, 0)],
                      5: [(0, -1), (-1, 0)],
                      6: [(0,1), (-1, 0)]
                     }
        visited = set()
        M, N = len(grid), len(grid[0])
        q = deque()
        q.append((0,0))
        while len(q) > 0:
            cell = q.popleft()
            i , j = cell[0], cell[1]
            if i == M-1 and j == N-1:
                return True
            if 0 <= i < M and 0 <= j < N and cell not in visited:
                visited.add(cell)
                direction = directions[grid[i][j]]
                cell1, cell2 = direction[0], direction[1]
                cell1 = (i + cell1[0], j + cell1[1])
                cell2 = (i + cell2[0], j + cell2[1])
                if cell1 not in visited :
                    q.append(cell1)
                if cell2 not in visited :
                    q.append(cell2)
        return False
            
s = Solution()
print(s.hasValidPath([[1,1,2]]))
print(s.hasValidPath([[2,4,3],[6,5,2]]))
print(s.hasValidPath([[1,2,1],[1,2,1]]))
        