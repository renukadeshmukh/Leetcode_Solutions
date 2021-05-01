'''
999. Available Captures for Rook

On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of 
white bishops 'B', black pawns 'p', and empty squares '.'. When the rook moves, 
it chooses one of four cardinal directions (north, east, south, or west), then 
moves in that direction until it chooses to stop, reaches the edge of the board, 
captures a black pawn, or is blocked by a white bishop. A rook is considered 
attacking a pawn if the rook can capture the pawn on the rook's turn. The number 
of available captures for the white rook is the number of pawns that the rook is 
attacking.
Return the number of available captures for the white rook.

Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: In this example, the rook is attacking all the pawns.

Input: board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation: The bishops are blocking the rook from attacking any of the pawns.

Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: The rook is attacking the pawns at positions b5, d6, and f5.
 
Constraints:
board.length == 8
board[i].length == 8
board[i][j] is either 'R', '.', 'B', or 'p'
There is exactly one cell with board[i][j] == 'R'
'''

'''
ALGORITHM:
1. Find position of Rook
2. Check North, South, East, West and look for valid pawns

RUNTIME COMPLEXITY: O(MN) + O(M) + O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        x, y = 0, 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x, y = i, j
                    break
        
        pawn_count = 0
        
        #north
        i,j = x-1,y
        while i >= 0:
            if board[i][j] == 'p':
                pawn_count += 1
                break
            elif board[i][j] == 'B':
                break
            else:
                i-= 1
        #south
        i,j = x+1,y
        while i < 8:
            if board[i][j] == 'p':
                pawn_count += 1
                break
            elif board[i][j] == 'B':
                break
            else:
                i+= 1
        #east
        i,j = x,y-1
        while j >= 0:
            if board[i][j] == 'p':
                pawn_count += 1
                break
            elif board[i][j] == 'B':
                break
            else:
                j-= 1
        #west
        i,j = x,y+1
        while j < 8:
            if board[i][j] == 'p':
                pawn_count += 1
                break
            elif board[i][j] == 'B':
                break
            else:
                j+= 1
        return pawn_count
                    
        