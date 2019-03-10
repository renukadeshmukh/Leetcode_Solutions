'''
780. Reaching Points

A move consists of taking a point (x, y) and transforming it to either (x, x+y) 
or (x+y, y).
Given a starting point (sx, sy) and a target point (tx, ty), return True if and 
only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). 
Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

Note:
sx, sy, tx, ty will all be integers in the range [1, 10^9].
'''

'''
ALGORITHM:
Basic idea:
If we start from sx,sy, it will be hard to find tx, ty.
If we start from tx,ty, we can find only one path to go back to sx, sy.

If 2 target points are still bigger than 2 starting point, reduce target points.
Check if we can reduce target points to (x, y+kx) or (x+ky, y)

RUNTIME COMPLEXITY: O(logN) where N = max(tx,ty)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        if tx == sx and ty == sy:
            return True
        elif tx < sx or ty < sy:
            return False
        elif tx == ty:
            return False 
        if tx == sx:
            if (ty-sy) % tx == 0:
                return True
            return False
        elif ty == sy:
            if (tx-sx) % ty == 0:
                return True
            return False
        elif tx > ty:
            return self.reachingPoints(sx, sy, tx-ty, ty)
        elif ty > tx:
            return self.reachingPoints(sx, sy, tx, ty-tx)



s = Solution()
print(s.reachingPoints(9, 10, 9, 19))
print(s.reachingPoints(1, 2, 999999999, 2))