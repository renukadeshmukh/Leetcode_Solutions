'''
1232. Check If It Is a Straight Line

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] 
represents the coordinate of a point. Check if these points make a straight line 
in the XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:
2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
'''

'''
ALGORITHM:
1. Calculate slope of all co-ordinates with the first co-ordinate. If all slope 
   values are same return True. Else return False.  

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x, y = coordinates[0][0], coordinates[0][1]
        x1, y1 = coordinates[1][0], coordinates[1][1]
        if y1 == y:
            slope = 'inf'
        else:
            slope = (x1 - x) / (y1 - y)
        
        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i][0], coordinates[i][1]
            if yi == y:
                slopei = 'inf'
            else:
                slopei = (xi - x) / (yi - y)
            if slope != slopei:
                return False
            
        return True
        

