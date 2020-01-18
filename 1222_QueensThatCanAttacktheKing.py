'''
1222. Queens That Can Attack the King

On an 8x8 chessboard, there can be multiple Black Queens and one White King.
Given an array of integer coordinates queens that represents the positions of 
the Black Queens, and a pair of coordinates king that represent the position of 
the White King, return the coordinates of all the queens (in any order) that can 
attack the King.

Example 1:
Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
Output: [[0,1],[1,0],[3,3]]
Explanation:  
The queen at [0,1] can attack the king cause they're in the same row. 
The queen at [1,0] can attack the king cause they're in the same column. 
The queen at [3,3] can attack the king cause they're in the same diagnal. 
The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1]. 
The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0]. 
The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.

Example 2:
Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
Output: [[2,2],[3,4],[4,4]]

Example 3:
Input: queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
Output: [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]
 
Constraints:
1 <= queens.length <= 63
queens[0].length == 2
0 <= queens[i][j] < 8
king.length == 2
0 <= king[0], king[1] < 8
At most one piece is allowed in a cell.
'''

'''
ALGORITHM:
1. Check all directions from the king, and break if a queen is found

RUNTIME COMPLEXITY: O(8*8)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        result = []
        tuples = set()
        for queen in queens:
            tuples.add((queen[0], queen[1]))
        print(tuples)  
        row, col = king[0], king[1]

        res = self.check_row(tuples, row, col)
        if res:
            result.extend(res)
        res = self.check_col(tuples, row, col)
        if res:
            result.extend(res)
        res = self.check_diagonal(tuples, row, col)
        if res:
            result.extend(res)
        
        return result

    def check_row(self, tuples, row, col):
        result = []
        #check left keeping row constant
        i = col-1
        while i >= 0:
            if (row,i) in tuples:
                result.append([row,i])
                break
            i -= 1
        #check right keeping row constant
        i = col+1
        while i < 8:
            if (row,i) in tuples:
                result.append([row,i])
                break
            i += 1
        return result

    def check_col(self, tuples, row, col):
        result = []
        #check top keeping column constant
        i = row-1
        while i >= 0:
            if (i,col) in tuples:
                result.append([i,col])
                break
            i -= 1
        #check down keeping column constant
        i = row+1
        while i < 8:
            if (i,col) in tuples:
                result.append([i,col])
                break
            i += 1
        return result

    def check_diagonal(self, tuples, row, col):
        result = []
        i,j = row-1, col-1
        while i>=0 and j>=0:
            if (i,j) in tuples:
                result.append([i,j])
                break
            i, j = i-1, j-1

        i,j = row+1, col-1
        while i<8 and j>=0:
            if (i,j) in tuples:
                result.append([i,j])
                break
            i, j = i+1, j-1

        i,j = row-1, col+1
        while i>=0 and j<8:
            if (i,j) in tuples:
                result.append([i,j])
                break
            i, j = i-1, j+1

        i,j = row+1, col+1
        while i<8 and j<8:
            if (i,j) in tuples:
                result.append([i,j])
                break
            i, j = i+1, j+1
        return result
    

s = Solution()
print(s.queensAttacktheKing(queens=[[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king=[0,0]))
#[[0,1],[1,0],[3,3]]
print(s.queensAttacktheKing(queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]))
#[[2,2],[3,4],[4,4]]
print(s.queensAttacktheKing([[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]))
#[[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]
