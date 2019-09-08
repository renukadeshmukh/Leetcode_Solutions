'''
130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions 
surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in that 
surrounded region.

Example:
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X

Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the 
border of the board are not flipped to 'X'. Any 'O' that is not on the border 
and it is not connected to an 'O' on the border will be flipped to 'X'. Two 
cells are connected if they are adjacent cells connected horizontally or 
vertically.
'''

'''
ALGORITHM:
1. Visit all borders and locate all 'O' on the borders. Enqueue neighbouring
   cells to a queue. board[i-1, j], board[i+1,j], board[i, j-1], board[i,j+1]
   Mark suck 'O' as '$'
2. While queue is not empty, dequeue next item. If entry at this cell == 'O',
   enqueu all neighbours again and change the value of this cell to '$'. 
3. Now you are left with all 'O' that are surrounded by 'X'
4. Iterate over the board and mark all 'O' to 'X'. Mark all '$' back to 'O'.

RUNTIME COMPLEXITY: O(N^2)
SPACE COMPLEXITY: O(N^2)
'''

from collections import deque

class Solution(object):
    def __init__(self):
        self.q = deque()
        
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m,n = len(board), len(board[0])
        self.mark_O_on_border(board)
        self.mark_all_O_connected_to_border(board)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '$':
                    board[i][j] = 'O'
        
    def mark_O_on_border(self, board):
        m,n = len(board), len(board[0])
        for j in range(n):
            if board[0][j] == 'O':
                board[0][j] = '$'
                self.add_connected_O_to_queue(m,n,0,j)
            if board[m-1][j] == 'O':
                board[m-1][j] = '$'
                self.add_connected_O_to_queue(m,n,m-1,j)
        
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = '$'
                self.add_connected_O_to_queue(m,n,i,0)
            if board[i][n-1] == 'O':
                board[i][n-1] = '$'
                self.add_connected_O_to_queue(m,n,i, n-1)
                
    def mark_all_O_connected_to_border(self, board):
        m,n = len(board), len(board[0])
        while len(self.q) > 0:
            cell = self.q.popleft()
            i, j = cell[0], cell[1]
            if board[i][j] == 'O':
                self.add_connected_O_to_queue(m,n,i,j)
                board[i][j] = '$'
         
                
    def add_connected_O_to_queue(self, m, n, i, j):
        if i >= 1:
            self.q.append([i-1, j])
        if i <= m-2:
            self.q.append([i+1, j])
        if j >= 1:
            self.q.append([i, j-1])
        if j <= n-2:
            self.q.append([i, j+1])
        
                
        