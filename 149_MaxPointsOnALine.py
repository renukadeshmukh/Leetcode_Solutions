'''
149. Max Points on a Line

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6

'''

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 2:
            return len(points)

        x = len(points) 
        slope_dict = {}
        visited = set()
        xy_dict = self.get_coordinate_count(points)
        for i in range(0, x-1):
            for j in range(i+1,x):
                x1,y1,x2,y2 = points[i].x, points[i].y, points[j].x, points[j].y
                p1 = "{0}_{1}".format(x1, y1)
                p2 = "{0}_{1}".format(x2, y2)
                m = self.get_slope_of_line(x1,y1,x2,y2)
                if m not in slope_dict:
                    slope_dict[m] = 0
                if p1 not in visited:
                    slope_dict[m] += xy_dict[p1]
                    visited.add(p1)
                if p2 not in visited:
                    slope_dict[m] += xy_dict[p2] 
                    visited.add(p2)
        return max(slope_dict.values())
    
    def get_slope_of_line(self, x1,y1,x2,y2):
        if x1 == x2:
            return "inf"
        return (y2-y1)/(x2-x1)
    

    def get_coordinate_count(self, points):
        xy_dict = {}
        for c in points:
            xy = "{0}_{1}".format(c.x, c.y)
            if xy in xy_dict:
                xy_dict[xy] += 1
            else:
                xy_dict[xy] = 1
        return xy_dict



arr = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
input = []
for a in arr:
    input.append(Point(a[0], a[1]))

print(Solution().maxPoints(input))

arr = [[1,1],[1,1],[2,3]]
input = []
for a in arr:
    input.append(Point(a[0], a[1]))


print(Solution().maxPoints(input))