'''
1138. Alphabet Board Path

On an alphabet board, we start at position (0, 0), corresponding to character 
board[0][0].
Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in 
the diagram below.

We may make the following moves:
'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on 
them.)
Return a sequence of moves that makes our answer equal to target in the minimum 
number of moves.  You may return any path that does so. 

Example 1:
Input: target = "leet"
Output: "DDR!UURRR!!DDD!"

Example 2:
Input: target = "code"
Output: "RR!DDRR!UUL!R!"

Constraints:
1 <= target.length <= 100
target consists only of English lowercase letters.
'''

'''
ALGORITHM:
1. to get row, column ofr a character from matrix, 
    row = (ord(ch) - 97) / 5
    row = (ord(ch) - 97) % 5
    becasue length of board is 5.
2. For every character, calculate target row, col
3. Find distance between source row, col and target row, col in terms of 
   U, D, R, L. 
4. 'z' is a special case as you cant go right from z. if target is z, first move 
   horizontally and then vertically. 


RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N^2)
'''

class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        r1,c1 = 0,0
        result = []
        for ch in target:
            r2,c2 = divmod(ord(ch)-97, 5)
            if r1 != r2 or c1 != c2:
                result.extend(self.generate_path(r1,c1,r2,c2,ch))
            result.append('!')
            r1,c1 = r2,c2
        return ''.join(result)
    
    def generate_path(self, r1, c1, r2, c2,ch):
        res = []
        vertical = self.move_vertical(r1, c1, r2, c2)
        horizontal = self.move_horizontal(r1, c1, r2, c2)
        if ch == 'z':
            res.extend(horizontal)
            res.extend(vertical)
        else: 
            res.extend(vertical)
            res.extend(horizontal)
        return res
    
    def move_horizontal(self, r1, c1, r2, c2):
        if c1 < c2:
            return ['R'] * (c2-c1)
        return ['L'] * (c1-c2)

    def move_vertical(self, r1, c1, r2, c2):
        if r1 < r2:
            return ['D'] * (r2-r1)
        return ['U'] * (r1-r2)

         
        
s = Solution()
print(s.alphabetBoardPath("leet"))
print(s.alphabetBoardPath("code"))