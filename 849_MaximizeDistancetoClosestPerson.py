'''
849. Maximize Distance to Closest Person

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 
There is at least one empty seat, and at least one person sitting. Alex wants to sit in the seat such 
that the distance between him and the closest person to him is maximized. Return that maximum distance 
to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1. 1 <= seats.length <= 20000
2. seats contains only 0s or 1s, at least one 0, and at least one 1.
'''

from math import ceil

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        distance = 0
        count = 0
        first = seats.index(1)
        last = self.lastIndex(seats, 1)
        lastdistance = len(seats)-last-1
        distance = max(first,lastdistance)
        #print(first, last)
        while first < last:
            if seats[first]==0:
                while seats[first]==0:
                    count=count+1
                    first=first+1
                distance = max(distance, int(ceil(count/2.0)))
                #print(count)
                count = 0
            else:
                first+=1
        return distance


    def lastIndex(self, seats, item):
        i = -1
        while seats[i] != item:
            i -= 1
        return len(seats) + i
        
s = Solution()
res = s.maxDistToClosest([1,0,0,0,1,0,1])
print(res)

#import pdb;pdb.set_trace()
res = s.maxDistToClosest([1,0,0,0])
print(res)