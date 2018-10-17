'''
593. Valid Square

Given the coordinates of four points in 2D space, return whether the four points 
could construct a square. The coordinate (x,y) of a point is represented by an 
integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
Note:
All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles 
(90-degree angles).
Input points have no order.
'''

'''
ALGORITHM:
1. Check if all sides are equal.
2. Check if side1^2 + side2^2 = diagonal^2
3. Ensure none of the sides have length 0

RUNTIME COMPLEXITY : O(1)
SPACE COMPLEXITY: O(1) 
'''

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        d1 = self.get_side_length(p1, p2)
        d2 = self.get_side_length(p1, p3)
        d3 = self.get_side_length(p1, p4)
        
        if d1 == d2 and  d1 + d2 == d3 and d1 != 0:
            d4 = self.get_side_length(p4, p2)
            d5 = self.get_side_length(p4, p3)
            if d1 == d4 == d5:
                return True
            return False
        elif d2 == d3 and d2 + d3 == d1 and d2 != 0:
            d4 = self.get_side_length(p2, p3)
            d5 = self.get_side_length(p2, p4)
            if d3 == d4 == d5:
                return True
            return False
        elif d1 == d3 and d1 + d3 == d2 and d1 != 0:
            d4 = self.get_side_length(p3, p2)
            d5 = self.get_side_length(p3, p4)
            if d3 == d4 == d5:
                return True
            return False
        else:
            return False
        
    #Calculate length between 2 co-ordinates    
    def get_side_length(self, c1, c2):
        d = (c2[1]-c1[1]) ** 2 + (c2[0]-c1[0]) ** 2
        return d
        
print(Solution().validSquare([0,0], [1,1], [1,0], [0,1]))