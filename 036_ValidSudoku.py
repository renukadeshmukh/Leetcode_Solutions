'''
36. Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be 
validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without 
repetition.

The Sudoku board could be partially filled, where empty cells are filled with 
the character '.'.

Example 1:
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
'''

'''
ALGORITHM:
1. Maintain sets for each row, column and gris in the matrix
2. For every element, if the element already exists in a row or col or grid,
   return False
3. Else return True

RUNTIME COMPLEXITY: O(1) (Runtime is O(81) for 81 cells in the matrix)
SPACE COMPLEXITY: O(1) (Space complexity is O(81) for 81 cells in the matrix)
'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_set = [set() for i in range(9)]
        col_set = [set() for i in range(9)]
        sub_box = [set() for i in range(9)]
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                c = board[i][j]
                if c != '.':
                    grid = self.getGridNum(i,j)
                    if c not in row_set[i] and c not in col_set[j] and \
                        c not in sub_box[grid]:
                        row_set[i].add(c)
                        col_set[j].add(c)
                        sub_box[grid].add(c)
                    else:
                        return False
        return True
        
        
    def getGridNum(self, i, j):
        majorRow = i / 3  # zero based majorRow
        majorCol = j / 3  # zero based majorCol
        return majorCol + majorRow * 3;