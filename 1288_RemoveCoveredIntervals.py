'''
1288. Remove Covered Intervals

Given a list of intervals, remove all intervals that are covered by another 
interval in the list. Interval [a,b) is covered by interval [c,d) if and only 
if c <= a and b <= d. After doing so, return the number of remaining intervals.

Example 1:
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
 
Constraints:
1 <= intervals.length <= 1000
0 <= intervals[i][0] < intervals[i][1] <= 10^5
intervals[i] != intervals[j] for all i != j
'''

'''
ALGORITHM:
1. Sort intervals by start time. 
2. there are now three possibilities for:
    > [x, y] and [x, y+z]
    > [x, y] and [m, n] where m > x and n < z (overlapping intervals)
    > [x, y] and [m, n] where m > x and n > z, (non-overlapping intervals)
3. For every pair of consecutive intervals, if case 1 or 3, increment answer.
4. Return answer.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x : x[0])
        
        last = intervals[0]
        cnt = 1
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] > last[0] and curr[1] > last[1]:
                last = curr
                cnt += 1
            elif last[0] == curr[0]:
                end = max(last[1], curr[1])
                last[1] = end
            
        return cnt
                
