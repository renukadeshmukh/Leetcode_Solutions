'''
1037. Valid Boomerang

A boomerang is a set of 3 points that are all distinct and not in a straight line.
Given a list of three points in the plane, return whether these points are a boomerang.

Example 1:
Input: [[1,1],[2,3],[3,2]]
Output: true

Example 2:
Input: [[1,1],[2,2],[3,3]]
Output: false

Note:
points.length == 3
points[i].length == 2
0 <= points[i][j] <= 100
'''

'''
ALGORITHM:
1. Calculate slope1, slope2 and slope3 for each pair of points. 
2. Check slope1 != slope2 != slope3

RUNTIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        slope1, slope2, slope3 = 'inf', 'inf', 'inf'
        a, b, c = points[0], points[1], points[2]
        #points a and b
        if a[1] != b[1]:
            slope1 = float(a[0]-b[0])/(a[1]-b[1])
        
        #points b and c
        if b[1] != c[1]:
            slope2 = float(b[0]-c[0])/(b[1]-c[1])
            
        #points a and c
        if a[1] != c[1]:
            slope3 = float(a[0]-c[0])/(a[1]-c[1])
        
        return slope1 != slope2 != slope3 != slope1

s = Solution()
print(s.isBoomerang([[0,0],[1,2],[0,1]]))
print(s.isBoomerang([[0,1],[0,2],[1,2]]))
print(s.isBoomerang([[1,1],[2,3],[3,2]]))
print(s.isBoomerang([[1,1],[2,2],[3,3]]))
print(s.isBoomerang([[0,0],[1,1],[1,1]]))