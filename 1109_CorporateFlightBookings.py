'''
1109. Corporate Flight Bookings

There are n flights, and they are labeled from 1 to n.

We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] 
means that we booked k seats from flights labeled i to j inclusive. Return an 
array answer of length n, representing the number of seats booked on each flight 
in order of their label.

Example 1:
Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
 
Constraints:
1 <= bookings.length <= 20000
1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
1 <= bookings[i][2] <= 10000
'''

'''
ALGORITHM:
1. Keep 2 arrays start and end of size len(booksings). 
2. For every booking in bookings, 
    start[i] += k
    end[j] += k
3. For answer[m] = answer[m-1] + start[m] - end[m]
   i.e., answer[m] = answer for previous flight + any new flights starting at 
   m - any flights ending at m

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        
        answer = [0] * n
        start, end = [0] * (n+1), [0] * (n+1)
        
        for booking in bookings:
            i, j, k = booking[0], booking[1], booking[2]
            start[i] += k
            end[j] += k
        
        last = 0
        for i in range(1, len(start)):
            answer[i-1] = last + start[i] - end[i-1]
            last = answer[i-1]
        
        return answer