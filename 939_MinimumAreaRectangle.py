'''
939. Minimum Area Rectangle

Given a set of points in the xy-plane, determine the minimum area of a rectangle 
formed from these points, with sides parallel to the x and y axes.
If there isn't any rectangle, return 0.

Example 1:
Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

Example 2:
Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2

Note:
1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
'''

'''
ALGORITHM:
1. For each pair of points in the array, consider them to be the long diagonal of 
   a potential rectangle. We can check if all 4 points are there using a Set.

   For example, if the points are (1, 1) and (5, 5), we check if we also have 
   (1, 5) and (5, 1). If we do, we have a candidate rectangle.

   Put all the points in a set. For each pair of points, if the associated 
   rectangle are 4 distinct points all in the set, then take the area of this 
   rectangle as a candidate answer.

RUNTIME COMPLEXITY: O(N^2)
SPACE COMPLEXITY: O(N)
'''
from sys import maxint 

class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        min_area = maxint
        pointset = set()
        for point in points:
            pointset.add((point[0],point[1]))
        
        n = len(points)
        for i in range(n-1):
            for j in range(i+1, n):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                if x1 != x2 and y1 != y2:
                    if (x2, y1) in pointset and (x1, y2) in pointset: 
                        area = (x1-x2) * (y1-y2)
                        min_area = min(abs(area), min_area)
        if min_area == maxint:
            return 0
        return min_area