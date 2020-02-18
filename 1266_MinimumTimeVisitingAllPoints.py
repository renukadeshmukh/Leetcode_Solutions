'''
1266. Minimum Time Visiting All Points

On a plane there are n points with integer coordinates points[i] = [xi, yi]. 
Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:
1. In one second always you can either move vertically, horizontally by one unit 
or diagonally (it means to move one unit vertically and one unit horizontally in 
one second).
2. You have to visit the points in the same order as they appear in the array.
 
Example 1:
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> 
                                                        [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds

Example 2:
Input: points = [[3,2],[-2,2]]
Output: 5

Constraints:
points.length == n
1 <= n <= 100
points[i].length == 2
-1000 <= points[i][0], points[i][1] <= 1000
'''

'''
ALGORITHM:
1. Iterate over the given points. 
2. Time takes to get from point p1 to point p2 is essentially :
    time = max(abs(x2-x1), abs(y2-y1))
3. Return summation of all times. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        time = 0
        for i in range(1, len(points)):
            #x1, y1 = points[i-1][0], points[i-1][1]
            #x2, y2 = points[i][0], points[i][1]
            x = abs(points[i][0] - points[i-1][0])
            y = abs(points[i][1] - points[i-1][1])
            time += max(x, y)
        return time
        

s = Solution()
print(s.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
