'''
447. Number of Boomerangs

Given n points in the plane that are all pairwise distinct, a "boomerang" is a 
tuple of points (i, j, k) such that the distance between i and j equals the 
distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and 
coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]
Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
'''

'''
ALGORITHM:
For each point, create a hashmap and count all points with same distance. 
If for a point p, there are k points with distance d, number of boomerangs 
corresponding to that are k*(k-1). Keep adding these to get the final result.

RUNTIME COMPLEXITY: O(N^2)
SPACE COMPLEXITY: O(N)
'''

from collections import defaultdict
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        
        for p in points:
            cmap = defaultdict(int)
            for q in points:
                dx = p[0]-q[0]
                dy = p[1]-q[1]
                d = dx*dx + dy*dy
                cmap[d] += 1
            for k in cmap:
                res += cmap[k] * (cmap[k] -1)
        return res


