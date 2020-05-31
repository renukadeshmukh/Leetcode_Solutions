'''
1275. Find Winner on a Tic Tac Toe Game

Tic-tac-toe is played by two players A and B on a 3 x 3 grid.
Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always 
places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, 
column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.

Given an array moves where each element is another array of size 2 corresponding 
to the row and column of the grid where they mark their respective character in 
the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a 
draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the 
grid is initially empty and A will play first.

Example 1:
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"

Example 2:
Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
"   "    "   "    "   "    "   "    "   "    "O  "

Example 3:
Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"

Example 4:
Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "

Constraints:
1 <= moves.length <= 9
moves[i].length == 2
0 <= moves[i][j] <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
'''

'''
ALGORITHM:
1. Generate regex for all winning combinations and winner. 
2. Maintain a 1-D array of length 9, to mark moves.
3. Iterate over moves and mark 'x' and 'o' as per input moves. 
4. Once all moves are marked, match against winning combinations. If match found,
   return a winner. 
5. If no winner found, but len(moves) < 9, tic-tac-toe is not complete yet. 
   Return Pending
6. Return Draw. 

RUNTIME COMPLEXITY: O(1) as max moves can be 9 as only 9 grids in tic-tac-toe
SPACE COMPLEXITY: O(1)
'''

import re
class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        winning_combinations = [
            ['^xxx......$', 'A'], ['^...xxx...$', 'A'], 
            ['^......xxx$', 'A'], ['^x..x..x..$', 'A'], ['^.x..x..x.$', 'A'], 
            ['^..x..x..x$', 'A'], ['^x...x...x$', 'A'], ['^..x.x.x..$', 'A'], 
            ['^ooo......$', 'B'], ['^...ooo...$', 'B'], ['^......ooo$', 'B'], 
            ['^o..o..o..$', 'B'], ['^.o..o..o.$', 'B'], ['^..o..o..o$', 'B'], 
            ['^o...o...o$', 'B'], ['^..o.o.o..$', 'B']
        ]
        
        tictactoe = ['.'] * 9
        players = ['x', 'o']
        player = 0
        for move in moves:
            cell = move[0] * 3 + move[1]
            tictactoe[cell] = players[player]
            player = player ^ 1 ^ 0
            
        
        moveset = ''.join(tictactoe)
        
        for combo in winning_combinations:
            regex = re.compile(combo[0])
            match = regex.match(moveset)
            if bool(match):
                return combo[1]
            
        if len(moves) < 9:
            return 'Pending'
        return 'Draw'
            

s = Solution()
print(s.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
print(s.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
print(s.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))
print(s.tictactoe([[0,0],[1,1]]))