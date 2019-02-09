'''
478. Generate Random Point in a Circle

Given the radius and x-y positions of the center of a circle, write a function 
randPoint which generates a uniform random point in the circle.

Note:

input and output values are in floating-point.
radius and x-y position of the center of the circle is passed into the class 
constructor. A point on the circumference of the circle is considered to be in 
the circle. RandPoint returns a size 2 array containing x-position and 
y-position of the random point, in that order.

Example 1:
Input: 
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

Example 2:
Input: 
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's 
constructor has three arguments, the radius, x-position of the center, and 
y-position of the center of the circle. randPoint has no arguments. Arguments 
are always wrapped with a list, even if there aren't any.
'''

'''
ALGORITHM:
1. Generate a random radius.
2. Generate a random theta (between 0 to 360)
3. Given new radius and angle, compute new x and y co-ordinates.

Note: https://stackoverflow.com/questions/5837572/generate-a-random-point-within-a-circle-uniformly

RUNTIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
'''
from random import random
from math import sin,cos, pi, sqrt

class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius, self.x, self.y = radius, x_center, y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        
        rand_radius = self.radius * sqrt(random())
        rand_theta = 2 * math.pi * random()
        x,y = self.x + rand_radius * cos(rand_theta), self.y + rand_radius * sin(rand_theta)
        return [x,y]
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()