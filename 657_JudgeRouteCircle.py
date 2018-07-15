'''
657. Judge Route Circle

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
'''

'''
Algorithm:
1. Iterate on each character
    > If R, x =  x+1
    > If L, x = x-1
    > If U, y = y+1
    > If D, y = y-1
2. If x=0 and y=0, then return True else False

TIME COMPLEXITY = O(n)
SPACE COMPLEXITY = O(1)
'''
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x,y = 0, 0

        for move in moves:
            if move == 'R':
                x = x+1
            elif move == 'L':
                x = x-1
            elif move == 'U':
                y = y+1
            elif move == 'D':
                y = y-1
        if x == 0 and y == 0:
            return True
        return False

s = Solution()
res = s.judgeCircle("UD")
print(res)
res = s.judgeCircle("LL")
print(res)
                
